# Generated by Django 3.2.14 on 2023-10-26 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0097_auto_20231025_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidforproject',
            old_name='assigned',
            new_name='accepted',
        ),
        migrations.DeleteModel(
            name='Hire',
        ),
    ]
