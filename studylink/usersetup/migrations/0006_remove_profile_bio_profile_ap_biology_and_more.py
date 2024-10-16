# Generated by Django 5.1 on 2024-10-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersetup', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Biology',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Chemistry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Environemental Science',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Language',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Literature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Physics 1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Physics C',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='AP Psychology',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Algebra 1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Algebra 2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Biology',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Calculus AB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Calculus BC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Chemistry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='English 1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='English 2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='English 3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='English 4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Geometry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Pre-Algebra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Pre-Calculus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.IntegerField(default='0123456789'),
        ),
    ]
