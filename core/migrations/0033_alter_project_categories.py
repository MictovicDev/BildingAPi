# Generated by Django 3.2.14 on 2023-09-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20230929_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.CharField(blank=True, choices=[('Skilledlabour', 'SL'), ('Supplier', 'SU')], max_length=500, null=True),
        ),
    ]