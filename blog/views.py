from django.shortcuts import render
from blog.models import Blog

# Page d'accueil du site
def index(request):
    posts = Blog.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts})
