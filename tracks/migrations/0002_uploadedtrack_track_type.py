# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedtrack',
            name='track_type',
            field=models.IntegerField(default=1, choices=[(1, b'SoundCloud'), (2, b'DropBox')]),
            preserve_default=True,
        ),
    ]
