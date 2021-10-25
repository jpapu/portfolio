from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length = 255)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='uncategorized')
    date_created = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')


    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #return to inidividual post after creation
        return reverse('home') #return to home after creation

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #return to inidividual post after creation
        return reverse('home') #return to home after creation


