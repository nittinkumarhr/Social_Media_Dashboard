# Generated by Django 3.1.3 on 2024-02-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20240203_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedpost',
            old_name='Post',
            new_name='post',
        ),
    ]
