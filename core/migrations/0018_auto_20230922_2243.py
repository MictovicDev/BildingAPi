# Generated by Django 3.2.14 on 2023-09-22 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20230922_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='request',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='request',
            name='image3',
        ),
    ]