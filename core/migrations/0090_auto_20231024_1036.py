# Generated by Django 3.2.14 on 2023-10-24 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20231024_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliersapplication',
            name='bid_for_items',
        ),
        migrations.AddField(
            model_name='item',
            name='supplier_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.suppliersapplication'),
        ),
    ]
