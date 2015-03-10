from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Article

def index(request):
	blog = Article.objects.all()
	return render(request, 'blog/detail.html', {'blog': blog[0]})
