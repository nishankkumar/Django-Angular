# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='other',
            name='user',
        ),
    ]
