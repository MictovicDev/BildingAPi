# Generated by Django 3.2.14 on 2023-09-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_user_bvnimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bvnimage',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
