# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('qualify', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
            ],
        ),
    ]
