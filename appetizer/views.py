from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from appetizer.forms import UserCreationForm

@login_required
def index(request):
   return render(request, 'quiz/index.html')

def account_create_view(request, **args):
	if request.method == 'POST':

		form = UserCreationForm(request.POST)

		if form.is_valid():
			return HttpResponsePermanentRedirect('/account/create/success/')

	else:
		form = UserCreationForm()

	return render(request, args.get('template'), {'form':form})
