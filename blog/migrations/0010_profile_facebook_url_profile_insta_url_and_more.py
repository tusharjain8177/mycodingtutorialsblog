# Generated by Django 4.0.4 on 2022-07-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='insta_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
