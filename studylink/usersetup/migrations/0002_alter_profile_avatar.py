# Generated by Django 5.1 on 2024-10-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='studylink\\static\\default.png', upload_to='profile_images'),
        ),
    ]
