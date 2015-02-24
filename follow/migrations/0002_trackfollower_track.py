# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackfollower',
            name='track',
            field=models.ForeignKey(to='tracks.UploadedTrack', unique=True),
            preserve_default=True,
        ),
    ]
