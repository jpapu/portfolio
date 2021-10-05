from typing import List
from django.shortcuts import render
from django.view.generic import ListView, DetailView
from portfolio.web_app.models import Post
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'