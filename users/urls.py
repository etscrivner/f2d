"""
    users.urls
    ~~~~~~~~~~
    Django URL routes related to users.

    Copyright (C) 2015 FollowToDownload
"""
from django.conf.urls import patterns, url

from users import views


urlpatterns = patterns('',
    url(r'^oauth/redirect', views.soundcloud_oauth_redirect, name='signup.oauth'),
    url(r'^oauth/callback', views.soundcloud_oauth_callback, name='signup.callback'),
    url(r'^dashboard', views.dashboard, name='dashboard')
)
