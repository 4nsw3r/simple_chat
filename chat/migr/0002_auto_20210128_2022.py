# Generated by Django 3.1.5 on 2021-01-28 17:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bl',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bl',
            field=models.ManyToManyField(blank=True, related_name='blacklist', to=settings.AUTH_USER_MODEL),
        ),
    ]
