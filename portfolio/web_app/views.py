from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_created']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')