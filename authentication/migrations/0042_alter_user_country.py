# Generated by Django 3.2.14 on 2023-10-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0041_auto_20231025_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('Algeria', 'Algeria'), ('Nigeria', 'Nigeria'), ('Egypt', 'Egypt'), ('South Africa', 'South Africa'), ('Morocco', 'Morocco'), ('Kenya', 'Kenya'), ('Ethiopia', 'Ethiopia'), ('Ghana', 'Ghana'), ('Cameroon', 'Cameroon'), ('Ghana', 'Ghana'), ('Tanzania', 'Tanzania'), ("Cote d'Ivoire", "Cote d'Ivoire")], max_length=250, null=True),
        ),
    ]