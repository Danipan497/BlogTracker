"""Defines url patterns for users."""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Login page.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout page.
    path('logout/', views.logout_view, name='logout'),

    # Registration page.
    path('register/', views.register, name='register'),

    # Password change.
    path('password/', auth_views.PasswordChangeView.as_view(template_name='users/password.html'), name='password'),
]
