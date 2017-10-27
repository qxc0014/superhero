# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timestamp',
            new_name='pub_date',
        ),
    ]
