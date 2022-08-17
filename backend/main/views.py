from multiprocessing import context
from django.shortcuts import render

from .models import Blog

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    blog = Blog.objects.all
    context = {
        'blog': blog,
    }
    return render(request, 'main/blog.html', context)


def contact(request):
    return render(request, 'main/contact.html')


def join(request):
    return render(request, 'main/join.html')


def talent(request):
    return render(request, 'main/talent.html')


def blogPost(request, slug):
    blog = Blog.objects.get(title=slug)
    context = {
        'blog': blog
    }
    return render(request, 'main/blogPost.html', context)


def model(request):
    return render(request, 'main/model.html')
