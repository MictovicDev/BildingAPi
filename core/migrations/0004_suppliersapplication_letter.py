# Generated by Django 4.2.5 on 2023-09-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_suppliersapplication_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliersapplication',
            name='letter',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
