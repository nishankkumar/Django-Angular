# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_other_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Other',
        ),
    ]
