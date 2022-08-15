from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def contact(request):
    return render(request, 'main/contact.html')


def join(request):
    return render(request, 'main/join.html')


def talent(request):
    return render(request, 'main/talent.html')


def blogPost(request):
    return render(request, 'main/blogPost.html')


def model(request):
    return render(request, 'main/model.html')
