# Generated by Django 3.2.14 on 2023-10-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_auto_20231026_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biditem',
            name='name',
        ),
    ]
