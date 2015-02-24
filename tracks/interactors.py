"""
    tracks.interactors
    ~~~~~~~~~~~~~~~~~~
    Interactors for tracks

    Copyright (C) 2015 FollowToDownload
"""
import uuid

from tracks import models


class TrackUploadInteractor(object):
    """Interactor for handling track uploading"""

    def run(self, user, artist, title, track_file):
        uploaded_track = models.UploadedTrack(
            track_url_id=str(uuid.uuid4()),
            user=user,
            artist=artist,
            title=title,
            track_file=track_file
        )
        uploaded_track.save()
        return uploaded_track
