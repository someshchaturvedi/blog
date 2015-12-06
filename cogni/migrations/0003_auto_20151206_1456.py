# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cogni', '0002_auto_20151205_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(default=b'this is a good blog', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
