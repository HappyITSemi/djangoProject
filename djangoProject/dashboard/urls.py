from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]
