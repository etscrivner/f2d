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
from tracks import interactors
from tracks import models
import users.gateways


logger = logging.getLogger(__name__)


class UploadView(generic.TemplateView):
    """View for uploading a new track for the current user."""
    template_name = 'tracks/upload.html'

    def post(self, request, *args, **kwargs):
        soundcloud_user_id = request.session.get('soundcloud_user_id')

        if not soundcloud_user_id:
            return shortcuts.redirect('homepage')

        user = users.gateways.DjangoSoundCloudUserDataGateway.get_by_soundcloud_user_id(
            soundcloud_user_id
        )

        upload_form = forms.UploadTrackForm(request.POST, request.FILES)

        if upload_form.is_valid():
            uploaded_track = interactors.TrackUploadInteractor().run(
                user,
                **upload_form.cleaned_data
            )
            context = {
                'uploaded_track': uploaded_track
            }
            return shortcuts.render(
                request, 'tracks/upload_success.html', context
            )

        context = self.get_context_data(**kwargs)
        context['form'] = upload_form
        return shortcuts.render(request, 'tracks/upload.html', context)

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context['upload'] = True
        context['form'] = forms.UploadTrackForm()
        return context


class InfoView(generic.TemplateView):
    """View for seeing track info"""
    template_name = 'tracks/info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        track_id = kwargs.get('track_id')
        context['track'] = models.UploadedTrack.objects.get(
            track_url_id=track_id
        )
        return context
