# Generated by Django 3.2.14 on 2023-10-24 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_suppliersapplication_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliersapplication',
            old_name='request',
            new_name='myrequest',
        ),
    ]
