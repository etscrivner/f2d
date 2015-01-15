# -*- coding: utf-8 -*-
"""
    tracks.models
    ~~~~~~~~~~~~~
    Django models related to uploaded tracks.

    Copyright (C) 2015 FollowToDownload
"""
from django.db import models

from tracks import entities
import users.models


class UploadedTrack(models.Model):
    """Represents an music track belonging to a user"""

    TRACK_TYPE_CHOICES = (
        (entities.TrackType.SoundCloud, 'SoundCloud'),
        (entities.TrackType.DropBox, 'DropBox')
    )

    uploaded_track_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(users.models.SoundCloudUser)
    artist = models.CharField(max_length=256, blank=False)
    title = models.CharField(max_length=256, blank=False)
    track_type = models.IntegerField(
        choices=TRACK_TYPE_CHOICES,
        blank=False,
        default=entities.TrackType.SoundCloud
    )
    track_url = models.URLField(blank=False)
    
    def as_entity(self):
        """Returns the entity form of the track.

        :rtype: tracks.entities.UploadedTrack
        """
        return entities.UploadedTrack(
            self.uploaded_track_id,
            self.user.id,
            self.artist,
            self.title,
            self.track_url
        )

    def __unicode__(self):
        """Returns the printed name for this entity

        :rtype: str or unicode
        """
        return u'(uploaded_track_id={}, user_id={})'.format(
            self.uploaded_track_id, self.user.id
        )
