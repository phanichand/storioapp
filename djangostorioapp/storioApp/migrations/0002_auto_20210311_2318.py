# Generated by Django 3.0.1 on 2021-03-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='story_page_audio',
            field=models.FileField(blank=True, null=True, upload_to='audios/'),
        ),
    ]
