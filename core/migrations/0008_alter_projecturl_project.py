# Generated by Django 3.2.14 on 2023-09-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20230922_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecturl',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='url', to='core.project'),
        ),
    ]
