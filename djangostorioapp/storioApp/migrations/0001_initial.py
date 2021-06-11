# Generated by Django 3.0.1 on 2021-03-11 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=200)),
                ('collection_cover_image', models.ImageField(upload_to='images/')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_name', models.CharField(max_length=200)),
                ('story_cover_image', models.ImageField(upload_to='images/')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storioApp.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='StoryPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_page_text', models.CharField(max_length=200)),
                ('story_page_image', models.ImageField(upload_to='images/')),
                ('story_page_audio', models.FileField(upload_to='audios/')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storioApp.Story')),
            ],
        ),
    ]
