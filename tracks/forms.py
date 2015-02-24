"""
    tracks.forms
    ~~~~~~~~~~~~
    Forms related to music tracks

    Copyright (C) 2015 FollowToDownload
"""
import logging

from django import forms
from django.conf import settings


logger = logging.getLogger(__name__)


class LimitedSizeFileField(forms.FileField):
    """A file field that raises an error if a maximum size is exceeded"""

    def __init__(self, *args, **kwargs):
        self.max_file_size_mb = kwargs.pop('max_file_size_mb')
        super(LimitedSizeFileField, self).__init__(*args, **kwargs)
    
    def clean(self, data, initial):
        max_file_size_bytes = (
            self.max_file_size_mb * 1E6
            if self.max_file_size_mb
            else None)
        if data and max_file_size_bytes and len(data) > max_file_size_bytes:
            raise forms.ValidationError(
                'File too large. Max size restricted to %r MB'
                % self.max_file_size_mb)
        return super(LimitedSizeFileField, self).clean(data, initial)


class UploadTrackForm(forms.Form):
    """Django form for for track file uploads"""

    artist = forms.CharField(max_length=256)
    title = forms.CharField(max_length=256)
    track_file = LimitedSizeFileField(
        max_file_size_mb=settings.MAX_TRACK_FILE_SIZE_MB,
        allow_empty_file=False)
