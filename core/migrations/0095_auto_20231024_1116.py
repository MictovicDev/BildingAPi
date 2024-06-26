# Generated by Django 3.2.14 on 2023-10-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0094_rename_request_suppliersapplication_myrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliersapplication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ApplicationImages/'),
        ),
        migrations.AlterField(
            model_name='biditem',
            name='supplier_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biditem', to='core.suppliersapplication'),
        ),
    ]
