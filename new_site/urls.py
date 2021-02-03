from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('sendmail/', include('sendmail.urls')),
    path('', include('new_sites.urls')),
]
