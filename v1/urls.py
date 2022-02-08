from django.urls import include
from django.urls import path

# /api/v1 の配下
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('user/', include('user.urls')),
]
