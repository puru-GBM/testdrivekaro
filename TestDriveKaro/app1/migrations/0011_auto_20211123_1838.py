# Generated by Django 3.2.9 on 2021-11-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20211123_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filter_luxury',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filter_top',
            name='Price',
            field=models.IntegerField(),
        ),
    ]