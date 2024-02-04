# Generated by Django 3.1.3 on 2024-02-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20240201_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]