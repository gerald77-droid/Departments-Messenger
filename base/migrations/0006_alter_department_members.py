# Generated by Django 4.2.6 on 2024-02-20 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
