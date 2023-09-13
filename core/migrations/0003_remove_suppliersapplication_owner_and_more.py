# Generated by Django 4.2.5 on 2023-09-13 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_suppliersapplication_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliersapplication',
            name='owner',
        ),
        migrations.AddField(
            model_name='image',
            name='supplierapplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.suppliersapplication'),
        ),
        migrations.AddField(
            model_name='suppliersapplication',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.store'),
        ),
    ]
