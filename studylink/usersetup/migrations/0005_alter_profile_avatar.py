# Generated by Django 5.1 on 2024-10-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersetup', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static\\default_profile.jpg', upload_to='profile_images'),
        ),
    ]
