# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-29 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_couchauditlogentry_courseauditlogentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='interested_form_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courseauditlogentry',
            name='interested_form_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Course price in 2 digits format. Example 23.45.', max_digits=5),
        ),
        migrations.AlterField(
            model_name='courseauditlogentry',
            name='course_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Course price in 2 digits format. Example 23.45.', max_digits=5),
        ),
    ]
