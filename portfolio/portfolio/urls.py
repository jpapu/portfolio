from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')),
    path('auth_app/', include('django.contrib.auth.urls')),
    path('auth_app/', include('auth_app.urls')),
]
