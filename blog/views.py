from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Article

def index(request):
	return render(request,'blog/index.html')

@login_required(login_url='/account/login/')
def detail(request):
	return render(request,'blog/detail.html')

@login_required(login_url='/account/login/')
def react_view(request):
	return render(request,'blog/react.html')
