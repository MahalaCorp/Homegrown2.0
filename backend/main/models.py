from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    coverImage = models.ImageField(upload_to='blog')
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)

    description = models.TextField()
    firstParagraph = models.TextField()
    secondParagraph = models.TextField(null=True)
    thirdParagraph = models.TextField(null=True)
    conclusion = models.TextField()

    image1 = models.ImageField(upload_to='blog')
    image2 = models.ImageField(upload_to='blog')
    image3 = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.title


class Talent(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='slug')
    coverImage = models.ImageField(upload_to='talent')
    height = models.IntegerField()
    waist = models.IntegerField()
    bust = models.IntegerField()
    shoe = models.IntegerField()
    dress = models.IntegerField()
    eye = models.CharField(max_length=255)
    hair = models.CharField(max_length=255)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TalentImage(models.Model):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="talent/img")
