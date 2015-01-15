"""
    tracks.forms
    ~~~~~~~~~~~~
    Forms related to music tracks

    Copyright (C) 2015 FollowToDownload
"""
import logging

from django import forms


logger = logging.getLogger(__name__)


class UploadTrackForm(forms.Form):
    """Django form for for track file uploads"""

    artist = forms.CharField(max_length=256)
    title = forms.CharField(max_length=256)
    track_url = forms.URLField()
