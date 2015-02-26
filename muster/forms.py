# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext, ugettext_lazy as _

from muster.contrib.captcha import CaptchaField
from jungle.settings import MIN_PASSWORD_LEN, CHECK_STRENGTH

_digit = set(map(chr, range(48, 58)))
_upper = set(map(chr, range(65, 91)))
_lower = set(map(chr, range(97,123)))

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class RegistrationForm(forms.Form):
	"""Form for creating new users. """
	username = forms.EmailField(
		required = True,
		label = "E-mail",
		max_length = 100,
		help_text = "This will be your login name.",
	)

	username_again = forms.EmailField(
		required = True,
		label = "E-mail (again)",
		help_text = "Make sure that this is a valid E-mail address.",
	)

	password = forms.CharField(
		required = True,
		label = "Password",
		widget = forms.PasswordInput(),
		help_text = "Use lower and upper case letters, numbers, etc.",
	)

	password_again = forms.CharField(
		required = True,
		label = "Password (again)",
		widget = forms.PasswordInput(),
	)

	first_name = forms.CharField(
		required = True,
		label = "First Name",
		help_text = "Enter your first name + middle name.",
	)

	def clean_first_name(self):
		first_name = self.cleaned_data['first_name']
		all_symbols = set(first_name)
		first_symbol = set(first_name[0])

		if ( first_symbol & _lower):
			raise forms.ValidationError('First letter must be Uppercase.')
		elif not ( all_symbols & _lower ):
			raise forms.ValidationError('Only CAPITALS are not allowed.')
		elif ( all_symbols & _digit ):
			raise forms.ValidationError('Digits are not allowed in first name.')

		return first_name

	last_name = forms.CharField(
		required = True,
		label = "Last Name",
		help_text = "Enter your last name.",
	)

	def clean_last_name(self):
		last_name = self.cleaned_data['last_name']
		all_symbols = set(last_name)
		first_symbol = set(last_name[0])

		if ( first_symbol & _lower):
			raise forms.ValidationError('First letter must be Uppercase.')
		elif not ( all_symbols & _lower ):
			raise forms.ValidationError('Only CAPITALS are not allowed.')
		elif ( all_symbols & _digit ):
			raise forms.ValidationError('Digits are not allowed in last name.')

		return last_name

	captcha = CaptchaField(
		required = True,
		label = "Security Code",
	)

	def clean_username(self):
		"""Make sure that `login` is unique in the system. """
		username = self.cleaned_data['username']

		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username

		raise forms.ValidationError('E-mail already in use.')

	def clean_username_again(self):
		"""Make sure that user verified `login` that he entered. """
		if 'username' in self.cleaned_data:
			username = self.cleaned_data['username']
			username_again = self.cleaned_data['username_again']

			if username == username_again:
				return username
			else:
				return None
			raise forms.ValidationError('E-mails do not match.')

	def clean_password(self):
		"""Make sure `password` isn't too easy to break. """
		password = self.cleaned_data['password']
		if CHECK_STRENGTH:
			if len(password) < MIN_PASSWORD_LEN:
				raise forms.ValidationError('Password must have at least %i characters.' % MIN_PASSWORD_LEN)

		symbols = set(password)
		if not ((_digit & symbols and _upper & symbols) or \
			(_digit & symbols and _lower & symbols) or \
			(_lower & symbols and _upper & symbols)):
			raise forms.ValidationError('Password is too weak, please choose a better one.')

		return password

	def clean_password_again(self):
		"""Make sure that the user verified the `password` he entered. """
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			password_again = self.cleaned_data['password_again']

		if password == password_again:
			return password
		else:
			return None
		raise forms.ValidationError('Passwords do not match.')

class LoginForm(forms.Form):
	"""Form for logging in users. """
	username = forms.CharField(
		required = True,
		label = "E-mail",
	)

	password = forms.CharField(
		required = True,
		label = u"",
		widget = forms.PasswordInput(),
	)

	def clean(self):
		"""Authenticate and login user, if possible. """
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')

		if username and password:
			self.user = authenticate(username=username, # XXX: actually email
				password=password)

			if self.user is not None:
				if self.user.is_active:
					return cleaned_data
				else:
					raise forms.ValidationError('Your account was disabled.')
					raise forms.ValidationError('Incorrect login name or password. Please try again.')

class ReminderForm(forms.Form):
	"""Password reminder form. """
	username = forms.CharField(
		required = True,
		label = "E-mail",
	)
	captcha = CaptchaField(
		required = True,
		label = "Security Code",
	)

	def clean_username(self):
		"""Make sure that `username` is registred in the system. """
		username = self.cleaned_data['username']

		try:
			User.objects.get(email=username)
		except ObjectDoesNotExist:
			raise forms.ValidationError('Selected user does not exist.')

		return username


class UserProfileForm(forms.Form):
	"""User profile form. """
	pass