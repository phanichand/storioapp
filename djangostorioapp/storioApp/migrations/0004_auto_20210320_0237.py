# Generated by Django 3.0.1 on 2021-03-20 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storioApp', '0003_storypage_story_page_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='story_page_text',
            field=models.CharField(max_length=500),
        ),
    ]