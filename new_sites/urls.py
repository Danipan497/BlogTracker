"""Defines url patterns for new_sites."""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'new_sites'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all about site.
    path('about/', views.about, name='about'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Show all success site.
    path('success/', views.success, name='success'),

    # Page for editing an entry.
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

