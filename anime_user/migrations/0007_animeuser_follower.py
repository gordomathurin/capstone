# Generated by Django 3.1.5 on 2021-01-11 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_user', '0006_delete_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='animeuser',
            name='follower',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]