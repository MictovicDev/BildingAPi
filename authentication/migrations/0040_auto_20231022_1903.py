# Generated by Django 3.2.14 on 2023-10-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0039_auto_20231022_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changepassword',
            name='newpassword',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='changepassword',
            name='oldpassword',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
