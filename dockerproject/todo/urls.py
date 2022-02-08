#
import debug_toolbar
from django.template.defaulttags import url
from django.urls import include
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoIndexView.as_view(), name='todo_index'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('create_category/', views.TodoCreateView.as_view(), name='todo_create_category'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='todo_delete'),
    # url(r'^__debug__/', include(debug_toolbar.urls)),
]
