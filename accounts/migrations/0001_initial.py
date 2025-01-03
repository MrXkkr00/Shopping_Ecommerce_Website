# Generated by Django 5.1.4 on 2024-12-24 14:59

import accounts.utils
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('address', models.TextField(verbose_name='Address')),
                ('username', models.CharField(blank=True, error_messages={'uniqeu': 'A user with that username already exists'}, max_length=150, null=True, verbose_name='username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
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
            name='VerificationOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(validators=[accounts.utils.check_otp_code], verbose_name='Otp code')),
                ('type', models.CharField(choices=[('register', 'Register'), ('reset_password', 'Reset password')], max_length=60, verbose_name='Verification Type')),
                ('expires_in', models.DateTimeField(auto_now_add=True, verbose_name='Expires in')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_otp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Verification Opt',
                'verbose_name_plural': 'Verification Opts',
            },
        ),
    ]
