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
