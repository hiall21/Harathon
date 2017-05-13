# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170513_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null='auth.User'),
        ),
    ]
