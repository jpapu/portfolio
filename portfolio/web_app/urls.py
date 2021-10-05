from django.urls import path
from web_app.views import HomeView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]