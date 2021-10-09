from django.urls import path
from web_app.views import CreatePostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]