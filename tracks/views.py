"""
    tracks.views
    ~~~~~~~~~~~~
    Django views for tracks

    Copyright (C) 2015 FollowToDownload
"""
from django import shortcuts
from django.views import generic


class UploadView(generic.TemplateView):
    """View for uploading a new track for the current user."""
    template_name = 'tracks/upload.html'
