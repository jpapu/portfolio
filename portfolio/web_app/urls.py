from django.urls import path
from web_app.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]