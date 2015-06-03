# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500)),
                ('mobile', models.CharField(max_length=50)),
                ('dob', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
