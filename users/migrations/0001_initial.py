# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoundCloudUser',
            fields=[
                ('soundcloud_user_id', models.AutoField(serialize=False, verbose_name=b'Internal ID', primary_key=True)),
                ('soundcloud_id', models.IntegerField(unique=True, verbose_name=b'SoundCloud ID', db_index=True)),
                ('access_token', models.CharField(max_length=256)),
                ('permalink', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('permalink_url', models.TextField()),
                ('avatar_url', models.TextField()),
                ('country', models.CharField(max_length=256, null=True, blank=True)),
                ('city', models.CharField(max_length=256, null=True, blank=True)),
                ('full_name', models.TextField()),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'SoundCloud User',
                'verbose_name_plural': 'SoundCloud Users',
            },
            bases=(models.Model,),
        ),
    ]
