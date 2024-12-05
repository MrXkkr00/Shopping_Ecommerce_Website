# Generated by Django 5.1.3 on 2024-12-05 06:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('apartment', models.CharField(max_length=120, verbose_name='Apartment')),
                ('street', models.TextField(verbose_name='Street')),
                ('pin_code', models.CharField(max_length=120, verbose_name='Pin Code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Address',
                'verbose_name_plural': 'User Addresses',
            },
        ),
        migrations.CreateModel(
            name='VerificationOpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Otp code')),
                ('type', models.CharField(choices=[('register', 'Register'), ('reset_password', 'Reset password')], max_length=60, verbose_name='Verification Type')),
                ('expires_in', models.DateTimeField(verbose_name='Expires in')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_otp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Verification Opt',
                'verbose_name_plural': 'Verification Opts',
            },
        ),
    ]
