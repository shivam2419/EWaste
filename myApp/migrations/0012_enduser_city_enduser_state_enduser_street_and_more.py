# Generated by Django 5.2.1 on 2025-05-24 06:58

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_alter_payments_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='enduser',
            name='state',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='enduser',
            name='street',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='enduser',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recycleform',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
