# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedTrack',
            fields=[
                ('uploaded_track_id', models.AutoField(serialize=False, primary_key=True)),
                ('artist', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('track_url', models.URLField()),
                ('user', models.ForeignKey(to='users.SoundCloudUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
