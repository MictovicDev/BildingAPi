# Generated by Django 3.2.14 on 2023-10-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_alter_bidforproject_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=300000, null=True),
        ),
    ]
