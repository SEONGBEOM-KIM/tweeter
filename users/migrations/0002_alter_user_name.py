# Generated by Django 5.0.2 on 2024-11-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='anonymous', max_length=150),
        ),
    ]
