# Generated by Django 3.1.5 on 2021-01-08 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import helpers.helper_file
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimePost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=helpers.helper_file.folder_path)),
                ('image_caption', models.TextField(max_length=600)),
                ('post_creation', models.DateField(default=django.utils.timezone.now)),
                ('anime_genre', models.CharField(choices=[('PICK_GENRE', 'CHOOSE GENRE'), ('SHONEN', 'SHONEN'), ('SHOUJU', 'SHOUJU'), ('SEINEN', 'SEINEN'), ('HAREM', 'HAREM'), ('ISEKAI', 'ISEKAI'), ('MECHA', 'MECHA'), ('SLICE_OF_LIFE', 'SLICE OF LIFE')], default='CHOOSE GENRE', max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('anime_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateField(default=django.utils.timezone.now)),
                ('anime_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='anime_post.animepost')),
            ],
        ),
    ]