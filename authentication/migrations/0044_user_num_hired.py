# Generated by Django 3.2.14 on 2023-10-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0043_alter_profile_bvn'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_hired',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
