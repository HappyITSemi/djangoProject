from django.urls import path
from . import views

app_name = 'batch'
urlpatterns = [
    path('', views.BatchIndexView.as_view(), name='batch_index'),
]
