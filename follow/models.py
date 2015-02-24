"""
    follow.models
    ~~~~~~~~~~~~~
    Models related to the follow-to-download functionality.

    Copyright (C) 2015 FollowToDownload
"""
from django.db import models

from follow import entities
import tracks.models


class SoundCloudFollower(models.Model):
    """Represents a user from soundcloud who came to follow"""
    
    class Meta:
        """Meta information regarding this model"""
        verbose_name = 'SoundCloud Follower'
        verbose_name_plural = 'SoundCloud Followers'

    soundcloud_follower_id = models.AutoField(
        primary_key=True, verbose_name='Internal ID'
    )
    soundcloud_id = models.IntegerField(
        db_index=True, blank=False, unique=True, verbose_name='SoundCloud ID'
    )
    access_token = models.CharField(max_length=256, blank=False)
    permalink = models.CharField(max_length=256, blank=False)
    username = models.CharField(max_length=256, blank=False)
    permalink_url = models.TextField(blank=False)
    avatar_url = models.TextField(blank=False)
    country = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    full_name = models.TextField(blank=False)

    def as_entity(self):
        """Returns the entity form of this model object.

        :rtype: follow.entities.SoundCloudFollower
        """
        return entities.SoundCloudFollower(
            soundcloud_follower_id=self.soundcloud_follower_id,
            soundcloud_id=self.soundcloud_id,
            access_token=self.access_token,
            permalink=self.permalink,
            username=self.username,
            permalink_url=self.permalink_url,
            avatar_url=self.avatar_url,
            country=self.country,
            city=self.city,
            full_name=self.full_name
        )

    def __unicode__(self):
        """Returns the printed name for this entity

        :rtype: str or unicode
        """
        return u'(soundcloud_follower_id={}, username={})'.format(
            self.soundcloud_follower_id, self.username
        )


class TrackFollower(models.Model):
    """Represents a new track follower"""
    
    track = models.ForeignKey(tracks.models.UploadedTrack, unique=True, db_index=True)
    follower = models.ForeignKey(SoundCloudFollower, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
