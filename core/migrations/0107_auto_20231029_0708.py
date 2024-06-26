# Generated by Django 3.2.14 on 2023-10-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0106_auto_20231029_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Files/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
