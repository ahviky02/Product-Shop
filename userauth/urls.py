from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]