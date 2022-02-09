import os

from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include
from django.urls import path

from . import settings
from .settings import BASE_DIR


def home(request):
    if request.method == 'GET':
        msg = {'message': 'Hello there'}
        return render(request, os.path.join(BASE_DIR, 'templates/index.html'), msg)

# comment-out path('admin/', admin.site.urls)


urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/', include('v1.urls')),
    path('todo/', include('todo.urls')),
    path('plot/', include('plot.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)