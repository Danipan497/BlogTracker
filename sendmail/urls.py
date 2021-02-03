from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sendmail'
urlpatterns = [
    path('contact/', views.contactView, name='contact'),
    # Show all success site.
    path('success/', views.success, name='success'),
]
