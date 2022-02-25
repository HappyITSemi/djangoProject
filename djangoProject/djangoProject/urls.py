import os

from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include
from django.urls import path

from . import settings
from .settings import BASE_DIR

from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)


def home(request):
    if request.method == 'GET':
        msg = {'message': 'Hello there'}
        return render(request, os.path.join(BASE_DIR, 'templates/index.html'), msg)


# comment-out path('admin/', admin.site.urls)

urlpatterns = [
                  path('', home, name='home'),
                  path('home/', home, name='home_root'),
                  path('admin/', admin.site.urls),

                  # すべてのアクション （⼀覧・詳細 ・登録・更新・⼀部更新・ 削除） をまとめて追加
                  path('api/', include(router.urls)),
                  path('todo/', include('todo.urls')),
                  path('plot/', include('plot.urls')),
                  path('batch/', include('batch.urls')),
                  path('accounts/', include('allauth.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
