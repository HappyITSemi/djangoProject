from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.home, "home"),
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
]

