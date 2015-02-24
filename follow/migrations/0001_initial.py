# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoundCloudFollower',
            fields=[
                ('soundcloud_follower_id', models.AutoField(serialize=False, verbose_name=b'Internal ID', primary_key=True)),
                ('soundcloud_id', models.IntegerField(unique=True, verbose_name=b'SoundCloud ID', db_index=True)),
                ('access_token', models.CharField(max_length=256)),
                ('permalink', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('permalink_url', models.TextField()),
                ('avatar_url', models.TextField()),
                ('country', models.CharField(max_length=256, null=True, blank=True)),
                ('city', models.CharField(max_length=256, null=True, blank=True)),
                ('full_name', models.TextField()),
            ],
            options={
                'verbose_name': 'SoundCloud Follower',
                'verbose_name_plural': 'SoundCloud Followers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackFollower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(to='follow.SoundCloudFollower', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
