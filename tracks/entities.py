# -*- coding: utf-8 -*-
"""
    tracks.entities
    ~~~~~~~~~~~~~~~
    Entities corresponding to track information.

    Copyright (C) 2015 FollowToDownload
"""


class UploadedTrack(object):
    """Entity representing a musical track"""

    def __init__(self,
                 uploaded_track_id,
                 track_url_id,
                 user_id,
                 artist,
                 title,
                 track_file):
        self.uploaded_track_id = uploaded_track_id
        self.track_url_id = track_url_id
        self.user_id = user_id
        self.artist = artist
        self.title = title
        self.track_file = track_file

    def __repr__(self):
        return "<UploadedTrack: uploaded_track_id={}>".format(
            self.uploaded_track_id
        )
