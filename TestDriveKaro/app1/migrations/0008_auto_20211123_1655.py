# Generated by Django 3.2.9 on 2021-11-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_filter_top_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter_luxury',
            name='img',
            field=models.ImageField(default='', upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='filter_top',
            name='img',
            field=models.ImageField(default='', upload_to='media/img'),
        ),
    ]
