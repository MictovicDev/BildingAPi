# Generated by Django 3.2.14 on 2023-10-12 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_auto_20231012_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project'),
        ),
    ]