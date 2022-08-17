import imp
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('join', views.join, name="join"),
    path('talent', views.talent, name="talent"),
    path('blogPost/<slug:slug>/', views.blogPost, name="blogPost"),
]
