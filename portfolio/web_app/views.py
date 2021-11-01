from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import CreatePostForm, EditPostForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu

        ind_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = ind_post.total_likes()
        context["total_likes"] = total_likes

        liked = False
        if ind_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["liked"] = liked
        return context

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_list': category_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')