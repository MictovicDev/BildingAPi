# Generated by Django 3.2.14 on 2023-09-27 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20230927_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.request'),
        ),
    ]
