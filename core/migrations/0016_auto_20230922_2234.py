# Generated by Django 3.2.14 on 2023-09-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20230922_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='request',
            name='image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='request',
            name='image3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
