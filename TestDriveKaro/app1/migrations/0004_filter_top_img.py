# Generated by Django 3.2.9 on 2021-11-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211123_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter_top',
            name='img',
            field=models.ImageField(height_field=150, null='true', upload_to='img', width_field=150),
            preserve_default='true',
        ),
    ]
