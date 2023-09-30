# Generated by Django 3.2.14 on 2023-09-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_recentproject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project',
        ),
        migrations.RemoveField(
            model_name='recentproject',
            name='image',
        ),
        migrations.AddField(
            model_name='recentproject',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.recentproject'),
        ),
    ]
