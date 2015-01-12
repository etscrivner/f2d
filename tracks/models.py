"""
    tracks.models
    ~~~~~~~~~~~~~
    Django models related to uploaded tracks.

    Copyright (C) 2015 FollowToDownload
"""
from django.db import models

import users.models


class UploadedTrack(models.Model):
    """Represents an uploaded music track belonging to a user"""

    uploaded_track_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(users.models.SoundCloudUser)
    track_file = models.FileField()
    
    def as_entity(self):
        """Returns the entity form of the track.

        :rtype: tracks.entities.UploadedTrack
        """
        raise NotImplementedError()

    def __unicode__(self):
        """Returns the printed name for this entity

        :rtype: str or unicode
        """
        return u'(uploaded_track_id={}, user_id=)'.format(
            self.uploaded_track_id, self.user.id
        )
