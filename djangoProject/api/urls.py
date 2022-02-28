#
from django.urls import path
from api import views


urlpatterns = [
    # URL パターンに <version> を含める
    path('books/', views.BookListAPIView.as_view()),
]
