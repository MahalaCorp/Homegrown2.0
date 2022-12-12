from multiprocessing import context
from statistics import mode
from django.shortcuts import render

from .models import Blog, Talent, TalentImage

# Create your views here.


def home(request):
    model = Talent.objects.all()
    blog = Blog.objects.all()
    context = {
        'blogs': blog,
        'models': model
    }
    return render(request, 'main/home.html', context)


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
    talents = Talent.objects.all()
    context = {
        'talents': talents
    }
    return render(request, 'main/talent.html', context)


def blogPost(request, slug):
    blog = Blog.objects.get(title=slug)
    context = {
        'blog': blog
    }
    return render(request, 'main/blogPost.html', context)


def model(request, slug):
    model = Talent.objects.get(slug=slug)
    image = TalentImage.objects.all()

    context = {
        'model': model,
        'image': image
    }
    return render(request, 'main/model.html', context)
