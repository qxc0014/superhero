# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default=14.21, max_length=150),
            preserve_default=False,
        ),
    ]
