# Generated by Django 3.2.14 on 2023-10-16 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0079_auto_20231016_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='reviews',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
