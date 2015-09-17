from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Article

@login_required(login_url='/account/login/')
def index(request):
	#blog = Article.objects.all()
	#return render(request, 'blog/detail.html', {'blog': blog[0]})
	return render(request,'blog/detail.html')
