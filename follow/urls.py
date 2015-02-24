"""
    follow.urls
    ~~~~~~~~~~~
    Django URL routes related to follow exchange.

    Copyright (C) 2015 FollowToDownload
"""
from django.conf.urls import patterns, url

from follow import views


urlpatterns = patterns('',
    url(r'^oauth/redirect', views.follow_oauth_redirect, name='follow.oauth.redirect'),
    url(r'^oauth/callback', views.follow_oauth_callback, name='follow.oauth.callback'),
    url(r'^create', views.create_follow_and_show_download, name='follow.create'),
    url(r'^(?P<track_id>.*)', views.follow_to_download_start, name='follow.start')
)
