from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:  # 対象のモデルクラスを指定
        model = Book  # 利⽤しないモデルのフィールドを
        exclude = ['created_at']
