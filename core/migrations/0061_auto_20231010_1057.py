# Generated by Django 3.2.14 on 2023-10-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_requestimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidforproject',
            name='applicationletter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bidforproject',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='Resume/'),
        ),
    ]