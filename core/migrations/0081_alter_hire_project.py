# Generated by Django 3.2.14 on 2023-10-16 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_auto_20231016_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hired', to='core.project'),
        ),
    ]
