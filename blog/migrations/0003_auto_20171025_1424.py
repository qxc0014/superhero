# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171025_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(default=14.2),
            preserve_default=False,
        ),
    ]
