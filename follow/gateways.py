"""
    users.gateways
    ~~~~~~~~~~~~~~
    Gateways to encapsulate access to entities.

    Copyright (C) 2015 FollowToDownload
"""
import datetime
import logging

import django.db

from follow import entities
from follow import models


logger = logging.getLogger(__name__)


class DjangoSoundCloudFollowerDataGateway(object):
    """Gateway to Django implementation of soundcloud follower"""

    @classmethod
    def get_by_soundcloud_follower_id(self, soundcloud_follower_id):
        """Return the follower with the given id.

        :param soundcloud_follower_id: A follower id
        :type soundcloud_follower_id: int
        :rtype: follow.entities.SoundCloudFollower
        """
        return models.SoundCloudFollower.objects.get(pk=soundcloud_follower_id)

    @classmethod
    def create_from_me_response(cls, obj):
        """Creates a new soundcloud follower from the given me route response.

        :param obj: The object returned from the route
        :type obj: dict
        :rtype: entities.SoundCloudFollower
        """
        soundcloud_follower, _ = models.SoundCloudFollower.objects.get_or_create(
            soundcloud_id=obj.get('id')
        )
        soundcloud_follower.access_token=obj.get('access_token')
        soundcloud_follower.permalink=obj.get('permalink')
        soundcloud_follower.username=obj.get('username')
        soundcloud_follower.permalink_url=obj.get('permalink_url')
        soundcloud_follower.avatar_url=obj.get('avatar_url')
        soundcloud_follower.country=obj.get('country')
        soundcloud_follower.city=obj.get('city')
        soundcloud_follower.full_name=obj.get('full_name')
        soundcloud_follower.last_login=datetime.datetime.utcnow()
        soundcloud_follower.save()
        return soundcloud_follower.as_entity()
