"""
    users.interactors
    ~~~~~~~~~~~~~~~~~
    Interactors related to users

    Copyright (C) 2015 FollowToDownload
"""
from users import gateways
from utils import client


class AuthenticateSoundCloudUserInteractor(object):
    """Interactor to authenticate a SoundCloudUser from a token exchange"""

    def __init__(self,
                 app_client=client.AppSoundCloudClient,
                 user_client=client.UserSoundCloudClient,
                 user_data_gateway=gateways.DjangoSoundCloudUserDataGateway):
        """Initialize the interactor with appropriate client interfaces."""
        self.app_client_cls = app_client
        self.user_client_cls = user_client
        self.user_data_gateway_cls = user_data_gateway

    def run(self, code):
        """Exchange the given code for an access token, creating a new user or
        returning an existing user.

        :param code: The temporary code
        :type code: str or unicode
        :rtype: 
        """
        access_token = self.app_client_cls().exchange_for_access_token(code)
        user_info = self.user_client_cls(access_token).get_me()
        entity = self.user_data_gateway_cls.create_from_me_response(user_info)
        return entity    
