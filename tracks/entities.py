# -*- coding: utf-8 -*-
"""
    tracks.entities
    ~~~~~~~~~~~~~~~
    Entities corresponding to track information.

    Copyright (C) 2015 FollowToDownload
"""


class TrackType(object):
    """The type of track this entities URL links to"""
    SoundCloud = 1
    DropBox = 2

    ALL = [SoundCloud, DropBox]

    @classmethod
    def is_valid(cls, track_type):
        """Indicates whether or not the given track type is valid.

        :track_type: A track type
        :track_type: int
        :rtype: bool
        """
        return track_type in cls.ALL


class UploadedTrack(object):
    """Entity representing a musical track"""

    def __init__(self, uploaded_track_id, user_id, artist, title, track_url):
        self.uploaded_track_id = uploaded_track_id
        self.user_id = user_id
        self.artist = artist
        self.title = title
        self.track_url = track_url

    def __repr__(self):
        return "<UploadedTrack: uploaded_track_id={}>".format(
            self.uploaded_track_id
        )
