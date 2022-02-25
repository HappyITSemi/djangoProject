import random
from abc import ABC

import rest_framework
from rest_framework import serializers
from rest_framework.serializers import ListSerializer
from django.utils import timezone

from api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:  # 対象のモデルクラスを指定
        model = Book  # 利⽤しないモデルのフィールドを
        fields = ['id', 'title', 'price']
        exclude = ['created_at']


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        pass

    # """複数の本モデルを扱うためのシリアライザ"""  #対象のシリアライザを指定
    child = BookSerializer()


class FortuneSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    # """今⽇の運勢を返すためのシリアライザ"""
    birth_date = serializers.DateField()
    blood_type = serializers.ChoiceField(choices=['A', 'B', 'O', 'AB'])  # 出⼒時に get_current_date() が呼ばれる
    current_date = serializers.SerializerMethodField()  # 出⼒時に get_fortune() が呼ばれる
    fortune = serializers.SerializerMethodField()

    def get_current_date(self, obj):
        return timezone.localdate()

    def get_fortune(self, obj):
        seed = '{}{}{}'.format(timezone.localdate(), obj['birth_date'], obj['blood_type'])
        random.seed(seed)
        return random.choice(['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★'])

