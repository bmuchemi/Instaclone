# Generated by Django 4.0.5 on 2022-06-05 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_image_profile_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='use',
            new_name='user',
        ),
    ]