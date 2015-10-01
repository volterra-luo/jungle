# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext, ugettext_lazy as _

# from muster.contrib.captcha import CaptchaField
# from jungle.settings import MIN_PASSWORD_LEN, CHECK_STRENGTH

_digit = set(map(chr, range(48, 58)))
_upper = set(map(chr, range(65, 91)))
_lower = set(map(chr, range(97,123)))

class UserCreationForm2(forms.Form):


	email = forms.EmailField(label=_("Email"),

		)

	username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})

	password = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)

	error_messages = {
		'duplicate_username': _(u'此用户名已存在,请输入新的用户名'),
	}

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User._default_manager.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code='duplicate_username'
		)



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
        fields = ('username',)

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
	username = forms.CharField(
		required = True,
		label = u'用户名',
		max_length = 100,
		help_text = u'这将是您的登录名',
	)

	def clean_username(self):
		"""Make sure that `login` is unique in the system. """
		username = self.cleaned_data['username']

		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username

		raise forms.ValidationError('Username already in use.')

	password = forms.CharField(
		required = True,
		label = u'密码',
		widget = forms.PasswordInput(),
		help_text = u'请使用大写字母，小写字母，数字等',
	)

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


	password_again = forms.CharField(
		required = True,
		label = u'密码确认',
		widget = forms.PasswordInput(),
	)

	def clean_password_again(self):
		"""Make sure that the user verified the `password` he entered. """
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			password_again = self.cleaned_data['password_again']

			if password == password_again:
				return password
			else:
				raise forms.ValidationError('Passwords do not match.')


	# captcha = CaptchaField(
	# 	required = True,
	# 	label = u'安全码',
	# )



class LoginForm(forms.Form):
	"""Form for logging in users. """
	username = forms.CharField(
		required = True,
		label = _("Username"),
	)

	password = forms.CharField(
		required = True,
		label = _('Password'),
		widget = forms.PasswordInput(),
	)

	def clean(self):
		"""Authenticate and login user, if possible. """
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')

		if username and password:
			self.user = authenticate(username=username, password=password)

			if self.user is not None:
				if self.user.is_active:
					return cleaned_data
				else:
					raise forms.ValidationError('Your account was disabled.')
					raise forms.ValidationError('Incorrect login name or password. Please try again.')


# class ReminderForm(forms.Form):
# 	"""Password reminder form. """
# 	username = forms.CharField(
# 		required = True,
# 		label = "E-mail",
# 	)
# 	captcha = CaptchaField(
# 		required = True,
# 		label = "Security Code",
# 	)

# 	def clean_username(self):
# 		"""Make sure that `username` is registred in the system. """
# 		username = self.cleaned_data['username']

# 		try:
# 			User.objects.get(email=username)
# 		except ObjectDoesNotExist:
# 			raise forms.ValidationError('Selected user does not exist.')

# 		return username



class UserProfileForm(forms.Form):
	"""User profile form. """
	pass
