# Generated by Django 4.2.3 on 2023-07-29 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
    ]
