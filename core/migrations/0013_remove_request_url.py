# Generated by Django 3.2.14 on 2023-09-22 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_project_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='url',
        ),
    ]