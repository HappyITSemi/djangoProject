# Generated by Django 4.0.2 on 2022-02-09 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
    ]
