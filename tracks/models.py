# -*- coding: utf-8 -*-
"""
    tracks.models
    ~~~~~~~~~~~~~
    Django models related to uploaded tracks.

    Copyright (C) 2015 FollowToDownload
"""
import uuid

from django.db import models

from tracks import entities
import users.models


class UploadedTrack(models.Model):
    """Represents an music track belonging to a user"""

    uploaded_track_id = models.AutoField(primary_key=True)
    track_url_id = models.CharField(
        max_length=36, blank=False, default=str(uuid.uuid4()), db_index=True
    )
    user = models.ForeignKey(users.models.SoundCloudUser, db_index=True)
    artist = models.CharField(max_length=256, blank=False)
    title = models.CharField(max_length=256, blank=False)
    track_file = models.FileField(blank=False)

    @property
    def downloads(self):
        """Compute and return the number of downloads for this track"""
        import follow.models
        return follow.models.TrackFollower.objects.filter(track=self)
    
    def as_entity(self):
        """Returns the entity form of the track.

        :rtype: tracks.entities.UploadedTrack
        """
        return entities.UploadedTrack(
            self.uploaded_track_id,
            self.track_url_id,
            self.user.id,
            self.artist,
            self.title,
            self.track_file
        )

    def __unicode__(self):
        """Returns the printed name for this entity

        :rtype: str or unicode
        """
        return u'(uploaded_track_id={}, user_id={})'.format(
            self.uploaded_track_id, self.user.pk
        )
