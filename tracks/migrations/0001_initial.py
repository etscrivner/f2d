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
                ('track_url_id', models.CharField(default=b'58886405-cb8e-4fc6-a1af-e669d654952e', max_length=36, db_index=True)),
                ('artist', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('track_file', models.FileField(upload_to=b'')),
                ('user', models.ForeignKey(to='users.SoundCloudUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
