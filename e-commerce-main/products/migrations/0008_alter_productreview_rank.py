# Generated by Django 5.0.6 on 2024-06-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productreview_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rank',
            field=models.IntegerField(verbose_name='rank'),
        ),
    ]
