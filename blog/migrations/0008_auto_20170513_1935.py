# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170513_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='author',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
