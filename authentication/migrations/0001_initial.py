# Generated by Django 4.2.5 on 2023-09-12 13:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('lastname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(choices=[('CO', 'Contractor'), ('SU', 'Supplier'), ('WO', 'Worker')], max_length=250)),
                ('location', models.CharField(blank=True, choices=[('ABJ', 'Abuja'), ('ABA', 'Aba'), ('AKR', 'Akure'), ('BNI', 'Benin City'), ('CAL', 'Calabar'), ('ENU', 'Enugu'), ('IBD', 'Ibadan'), ('ILR', 'Ilorin'), ('JOS', 'Jos'), ('KAD', 'Kaduna'), ('KAN', 'Kano'), ('LAG', 'Lagos'), ('MAI', 'Maiduguri'), ('OWE', 'Owerri'), ('PHC', 'Port Harcourt'), ('SKT', 'Sokoto'), ('UYO', 'Uyo'), ('WRR', 'Warri'), ('ONI', 'Onitsha'), ('OSB', 'Osogbo')], max_length=250, null=True)),
                ('bvn', models.BigIntegerField(null=True)),
                ('hires', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
