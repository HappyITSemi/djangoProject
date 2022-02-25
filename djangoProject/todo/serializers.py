from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo  # 利⽤するモデルのフィールド
        fields = ['id',
                  'name',
                  'description',
                  'due_date',
                  'created_at',
                  'updated_at',
                  'category_id',
                  ]
