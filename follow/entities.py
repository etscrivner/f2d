"""
    follow.entities
    ~~~~~~~~~~~~~~~
    Entities (from Entity-Interactor pattern) representing follow-related
    objects.

    Copyright (C) 2015 FollowToDownload
"""


class SoundCloudFollower(object):
    """Database agnostic entity representation of a soundcloud follower."""
    
    def __init__(self,
                 soundcloud_follower_id,
                 soundcloud_id,
                 access_token,
                 permalink,
                 username,
                 permalink_url,
                 avatar_url,
                 country,
                 city,
                 full_name):
        self.soundcloud_follower_id = soundcloud_follower_id
        self.soundcloud_id = soundcloud_id
        self.access_token = access_token
        self.permalink = permalink
        self.username = username
        self.permalink_url = permalink_url
        self.avatar_url = avatar_url
        self.country = country
        self.city = city
        self.full_name = full_name

    def as_json(self):
        """Return the entity in a JSON serializable format
        
        :rtype: dict
        """
        return {
            'id': self.soundcloud_follower_id,
            'soundcloud_id': self.soundcloud_id,
            'access_token': self.access_token,
            'permalink': self.permalink,
            'username': self.username,
            'permalink_url': self.permalink_url,
            'avatar_url': self.avatar_url,
            'country': self.country,
            'city': self.city,
            'full_name': self.full_name,
        }
