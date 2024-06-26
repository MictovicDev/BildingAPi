# Generated by Django 3.2.14 on 2023-10-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20231003_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='request',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='request',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='request',
            name='category',
            field=models.CharField(blank=True, choices=[('Electrical', 'Electrical'), ('Plumbing', 'Plumbing'), ('Construction', 'Construction'), ('Plastering', 'Plastering'), ('Painting', 'Painting'), ('InteriorDecoration', 'InteriorDecoration')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
