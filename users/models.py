"""
    users.models
    ~~~~~~~~~~~~
    Django user database models

    Copyright (C) 2015 FollowToDownload
"""
from django.db import models

from users import entities


class SoundCloudUser(models.Model):
    """Django model equivalent to our user entity"""

    class Meta:
        """Meta information regarding this model"""
        verbose_name = 'SoundCloud User'
        verbose_name_plural = 'SoundCloud Users'
        
    soundcloud_user_id = models.AutoField(
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
    last_login = models.DateTimeField(null=True, blank=False)

    def num_follows_last_seven_days(self):
        """Return the number of follows for the last 7 days.

        :rtype: int
        """
        import tracks.models
        import follow.models
        my_tracks = tracks.models.UploadedTrack.objects.filter(user=self)
        return follow.models.TrackFollower.objects.filter(track=my_tracks).count()

    def as_entity(self):
        """Returns the entity form of this model object.

        :rtype: users.entities.SoundCloudUser
        """
        return entities.SoundCloudUser(
            soundcloud_user_id=self.soundcloud_user_id,
            soundcloud_id=self.soundcloud_id,
            access_token=self.access_token,
            permalink=self.permalink,
            username=self.username,
            permalink_url=self.permalink_url,
            avatar_url=self.avatar_url,
            country=self.country,
            city=self.city,
            full_name=self.full_name,
            last_login=self.last_login
        )

    def __unicode__(self):
        """Returns the printed name for this entity

        :rtype: str or unicode
        """
        return u'(soundcloud_user_id={}, username={})'.format(
            self.soundcloud_user_id, self.username
        )
