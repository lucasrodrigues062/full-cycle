# Generated by Django 5.1.2 on 2024-10-22 00:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/', verbose_name='Thumbnail')),
                ('slug', models.SlugField(unique=True)),
                ('published_at', models.DateTimeField(editable=False, null=True, verbose_name='Publicado em')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicado')),
                ('num_likes', models.IntegerField(default=0, editable=False, verbose_name='Likes')),
                ('num_views', models.IntegerField(default=0, editable=False, verbose_name='Visualizações')),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='videos', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('tags', models.ManyToManyField(related_name='videos', to='core.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='VideoMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_path', models.CharField(max_length=255, verbose_name='Vídeo')),
                ('status', models.CharField(choices=[('UPLOADED_STARTED', 'Upload Iniciado'), ('PROCESSING_STARTED', 'Processamento Iniciado'), ('PROCESSING_FINISHED', 'Processamento Finalizado'), ('PROCESSING_ERROR', 'Erro no Processamento')], default='UPLOADED_STARTED', max_length=20, verbose_name='Status')),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='video_media', to='core.video', verbose_name='Vídeo')),
            ],
        ),
    ]
