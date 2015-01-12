"""
    users.gateways
    ~~~~~~~~~~~~~~
    Gateways to encapsulate access to entities.

    Copyright (C) 2015 FollowToDownload
"""
import datetime
import logging

import django.db

from users import entities
from users import models


logger = logging.getLogger(__name__)


class DjangoSoundCloudUserDataGateway(object):
    """Gateway to Django implementation of soundcloud user"""

    @classmethod
    def get_by_soundcloud_user_id(self, soundcloud_user_id):
        """Return the user with the given id.

        :param soundcloud_user_id: A user id
        :type soundcloud_user_id: int
        :rtype: models.entities.SoundCloudUser
        """
        return models.SoundCloudUser.objects.get(pk=soundcloud_user_id)

    @classmethod
    def create_from_me_response(cls, obj):
        """Creates a new soundcloud user from the given me route response.

        :param obj: The object returned from the route
        :type obj: dict
        :rtype: entities.SoundCloudUser
        """
        soundcloud_user, _ = models.SoundCloudUser.objects.get_or_create(
            soundcloud_id=obj.get('id')
        )
        soundcloud_user.access_token=obj.get('access_token')
        soundcloud_user.permalink=obj.get('permalink')
        soundcloud_user.username=obj.get('username')
        soundcloud_user.permalink_url=obj.get('permalink_url')
        soundcloud_user.avatar_url=obj.get('avatar_url')
        soundcloud_user.country=obj.get('country')
        soundcloud_user.city=obj.get('city')
        soundcloud_user.full_name=obj.get('full_name')
        soundcloud_user.last_login=datetime.datetime.utcnow()
        soundcloud_user.save()
        return soundcloud_user.as_entity()
