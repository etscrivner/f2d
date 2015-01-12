"""
    users.views
    ~~~~~~~~~~~
    Django views related to users.

    Copyright (C) 2015 FollowToDownload
"""
import logging

from django import shortcuts
from django.contrib import auth
import soundcloud

from f2d import settings
from users import gateways
from users import interactors
from users import models
from utils import client


logger = logging.getLogger(__name__)


def soundcloud_oauth_redirect(request):
    """Redirect user to soundcloud OAuth screen."""
    return shortcuts.redirect(client.AppSoundCloudClient().get_oauth_url())


def soundcloud_oauth_callback(request):
    """The callback after the user has signed in with soundcloud."""
    code = request.GET.get('code')

    if not code:
        return shortcuts.redirect('homepage')

    user = interactors.AuthenticateSoundCloudUserInteractor().run(code)
    request.session['soundcloud_user_id'] = user.soundcloud_user_id
    return shortcuts.redirect('dashboard')


def dashboard(request):
    """Display the user dashboard"""
    soundcloud_user_id = request.session.get('soundcloud_user_id')

    if not soundcloud_user_id:
        return shortcuts.redirect('homepage')

    user = gateways.DjangoSoundCloudUserDataGateway.get_by_soundcloud_user_id(
        soundcloud_user_id
    )
    context = {'user': user}

    return shortcuts.render(request, 'dashboard.html', context)
