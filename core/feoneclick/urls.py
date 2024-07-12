from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    # Acount #######################################################
    path('', lambda request: redirect('dashboard/', permanent=True)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.Profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)