"""
    follow.views
    ~~~~~~~~~~~~
    Django views related to follow functionality.

    Copyright (C) 2015 FollowToDownload
"""
import logging

from django import db
from django import shortcuts
import requests

import tracks.models
from follow import gateways
from follow import models
from users import interactors
from utils import client


logger = logging.getLogger(__name__)


def follow_to_download_start(request, track_id):
    """Follow Start - Step (1) of follow to download process"""
    if not track_id:
        return shortcuts.redirect('homepage')

    track = tracks.models.UploadedTrack.objects.get(track_url_id=track_id)

    if not track:
        return shortcuts.redirect('homepage')

    if 'soundcloud_follower_id' in request.session:
        return render_follow_page(request, track)
    elif 'follow_id' in request.session:
        return render_download_page(request, track)
    
    return shortcuts.render(
        request, 'follow/first_step.html', {'track': track}
    )


def render_follow_page(request, track):
    """Render the page to get the users follow"""
    follower = gateways.DjangoSoundCloudFollowerDataGateway.get_by_soundcloud_follower_id(
        request.session['soundcloud_follower_id']
    )

    if not follower:
        return shortcuts.redirect(
            'follow.start', track_id=request.session['track_id']
        )

    return shortcuts.render(
        request,
        'follow/second_step.html',
        {'track': track, 'follower': follower}
    )


def create_follow_and_show_download(request):
    """Create the follow for the current user"""
    if 'track_id' not in request.GET:
        return shortcuts.redirect('homepage')

    if 'soundcloud_follower_id' not in request.session:
        return shortcuts.redirect('homepage')

    track = tracks.models.UploadedTrack.objects.get(
        track_url_id=request.GET['track_id']
    )
    follower = gateways.DjangoSoundCloudFollowerDataGateway.get_by_soundcloud_follower_id(
        request.session['soundcloud_follower_id']
    )

    del request.session['soundcloud_follower_id']

    if not all([track, follower]):
        return request.redirect('homepage')

    user_client = client.UserSoundCloudClient(
        access_token=follower.access_token
    )

    try:
        user_client.add_follower(track.user.soundcloud_id)
    except requests.HTTPError as http_error:
        logger.error(http_error)
        return shortcuts.redirect('homepage')

    try:
        models.TrackFollower(follower=follower, track=track).save()
    except db.IntegrityError:
        # This user has already followed this track.
        pass

    return shortcuts.render(
        request,
        'follow/download.html',
        {'track': track}
    )


def follow_oauth_redirect(request):
    """Redirect to follow connect app"""
    if u'track_id' not in request.GET:
        shortcuts.redirect('homepage')

    request.session['track_id'] = request.GET['track_id']

    return shortcuts.redirect(
        client.AppSoundCloudFollowerClient().get_oauth_url()
    )


def follow_oauth_callback(request):
    """Handle user who has authenticated our app"""
    code = request.GET.get('code')

    if not code:
        return shortcuts.redirect('homepage')

    if 'track_id' not in request.session:
        return shortcuts.redirect('homepage')

    user = interactors.AuthenticateSoundCloudUserInteractor(
        app_client=client.AppSoundCloudFollowerClient,
        user_data_gateway=gateways.DjangoSoundCloudFollowerDataGateway
    ).run(code)
    request.session['soundcloud_follower_id'] = user.soundcloud_follower_id

    return shortcuts.redirect(
        'follow.start', track_id=request.session['track_id']
    )
