from django.urls import path
#from web_app.views import HomeView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    #path('', HomeView.as_view(), name='home'),
]