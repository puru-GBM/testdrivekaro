# Generated by Django 3.2.9 on 2021-11-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20211123_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter_luxury',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='filter_top',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
    ]