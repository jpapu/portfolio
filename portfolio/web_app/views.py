from typing import List
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from.forms import CreatePostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')