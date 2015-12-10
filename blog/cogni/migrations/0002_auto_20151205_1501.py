# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cogni', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
