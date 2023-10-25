# Generated by Django 3.2.14 on 2023-10-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0040_auto_20231022_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('United States', 'United States'), ('Canada', 'Canada'), ('United Kingdom', 'United Kingdom'), ('France', 'France'), ('Germany', 'Germany'), ('Australia', 'Australia'), ('Brazil', 'Brazil'), ('China', 'China'), ('India', 'India'), ('Japan', 'Japan'), ('South Korea', 'South Korea'), ('Mexico', 'Mexico'), ('Nigeria', 'Nigeria'), ('Russia', 'Russia'), ('Saudi Arabia', 'Saudi Arabia'), ('South Africa', 'South Africa'), ('Argentina', 'Argentina'), ('Egypt', 'Egypt'), ('Italy', 'Italy'), ('Spain', 'Spain'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Greece', 'Greece'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Kuwait', 'Kuwait'), ('Malaysia', 'Malaysia'), ('Pakistan', 'Pakistan'), ('Philippines', 'Philippines'), ('Singapore', 'Singapore'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('Vietnam', 'Vietnam'), ('Bangladesh', 'Bangladesh'), ('Netherlands', 'Netherlands'), ('Poland', 'Poland'), ('Sweden', 'Sweden'), ('Ukraine', 'Ukraine')], max_length=250, null=True),
        ),
    ]