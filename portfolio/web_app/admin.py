from django.contrib import admin
from .models import Category, Comment, Post, UserProfile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)

