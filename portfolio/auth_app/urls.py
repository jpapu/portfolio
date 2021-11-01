from django.urls import path
from .views import CreateProfilePageView, EditProfilePageView, ShowProfilePageView, UserRegisterView, UserSettingsView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserSettingsView.as_view(), name='edit_settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name ="password_success"),
    path('<int:pk>/user_profile/', ShowProfilePageView.as_view(), name ="show_profile_page"),
    path('<int:pk>/edit_user_profile/', EditProfilePageView.as_view(), name ="edit_user_profile"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name ="create_profile_page"),
]