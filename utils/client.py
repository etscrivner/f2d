"""
    utils.client
    ~~~~~~~~~~~~
    Soundcloud clients

    Copyright (C) 2015 FollowToDownload
"""
import logging

import soundcloud

from f2d import errors
from f2d import settings


logger = logging.getLogger(__name__)


class AppSoundCloudClient(object):
    """Interface for interacting with soundcloud as our application"""

    class AccessTokenError(errors.Error):
        """Exception raised when token exchange fails"""
        pass

    def __init__(self, soundcloud_client=soundcloud.Client):
        """Initializes the soundcloud client

        :param soundcloud_client: The soundcloud client to use (mostly for test
                                  mocking)
        """
        self.client = soundcloud_client(
            client_id=settings.SOUNDCLOUD_CLIENT_ID,
            client_secret=settings.SOUNDCLOUD_CLIENT_SECRET,
            redirect_uri=settings.SOUNDCLOUD_REDIRECT_URI
        )

    def get_oauth_url(self):
        """Return the URL to send the user to when requesting app
        authorization.

        :rtype: str or unicode
        """
        return self.client.authorize_url()

    def exchange_for_access_token(self, code):
        """Exchange the given temporary code for an access token.

        :param code: The temporary authorization code
        :type code: str or unicode
        :return: The access token received
        :rtype: str or unicode
        """
        resource = self.client.exchange_token(code)
        data = resource.obj

        if u'access_token' not in data:
            raise self.AccessTokenError(
                'Access token not found in response {!r}'.format(data)
            )

        logger.info(
            'Exchanged code %s for token %s', code, data[u'access_token']
        )

        return data[u'access_token']


class UserSoundCloudClient(object):
    """Interface for interacting with soundcloud as a specific user"""

    def __init__(self, access_token, soundcloud_client=soundcloud.Client):
        """Initialize the user soundcloud client.

        :param soundcloud_client: The soundcloud client to use (mostly for test
                                  mocking)
        :param access_token: The users access token.
        :type access_token: str or unicode
        """
        self.client = soundcloud_client(access_token=access_token)
        self.access_token = access_token

    def get_me(self):
        """Return the data from /me

        :rtype: dict
        """
        resource = self.client.get('/me')
        data = resource.obj
        data[u'access_token'] = self.access_token
        return data
