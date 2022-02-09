# Generated by Django 4.0.2 on 2022-02-09 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('todo', '0001_initial')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリー名')),
            ],
            options={
                'verbose_name_plural': 'Category',
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='タイトル名')),
                ('description', models.CharField(max_length=32, verbose_name='内容')),
                ('due_date', models.DateTimeField(verbose_name='期限')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.category', verbose_name='カテゴリー選択')),
                # ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Todo',
                'db_table': 'todo',
                'managed': True,
            },
        ),
    ]
