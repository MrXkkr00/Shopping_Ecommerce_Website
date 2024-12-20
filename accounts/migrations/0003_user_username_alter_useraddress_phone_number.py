# Generated by Django 5.1.3 on 2024-12-08 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email_useraddress_verificationopt'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')], verbose_name='Phone Number'),
        ),
    ]
