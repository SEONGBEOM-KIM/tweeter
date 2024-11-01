# Generated by Django 5.0.2 on 2024-11-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='lanaguage',
            field=models.CharField(choices=[('kr', 'Korean'), ('en', 'English')], default='kr', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
