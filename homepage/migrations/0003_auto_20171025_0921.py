# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20171025_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='department',
            field=models.CharField(blank=True, choices=[('An', 'Android'), ('Py', 'Python Django'), ('BA', 'Business Analyst'), ('HR', 'HR')], max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='n_attempts',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='result',
            field=models.CharField(blank=True, choices=[('p', 'Pass'), ('f', 'fail'), ('w', 'waiting_list')], max_length=100),
        ),
    ]