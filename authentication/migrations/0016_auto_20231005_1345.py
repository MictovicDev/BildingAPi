# Generated by Django 3.2.14 on 2023-10-05 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_user_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bvn',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gov_id_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hires',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.CreateModel(
            name='UpdateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bvn', models.PositiveBigIntegerField(null=True)),
                ('hires', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('gov_id_image', models.FileField(null=True, upload_to='files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
