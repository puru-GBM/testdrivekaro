# Generated by Django 3.2.9 on 2021-11-23 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20211123_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='companyname',
            new_name='Subject',
        ),
    ]