"""
    tracks.views
    ~~~~~~~~~~~~
    Django views for tracks

    Copyright (C) 2015 FollowToDownload
"""
import logging

from django import shortcuts
from django.views import generic

from tracks import forms


logger = logging.getLogger(__name__)


class UploadView(generic.TemplateView):
    """View for uploading a new track for the current user."""
    template_name = 'tracks/upload.html'

    def post(self, request, *args, **kwargs):
        upload_form = forms.UploadTrackForm(request.POST)

        if upload_form.is_valid():
            return shortcuts.render(request, 'tracks/upload_success.html', {})

        context = self.get_context_data(**kwargs)
        context['form'] = upload_form
        return shortcuts.render(request, 'tracks/upload.html', context)

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context['upload'] = True
        context['form'] = forms.UploadTrackForm()
        return context
