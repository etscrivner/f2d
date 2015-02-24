"""
    tracks.urls
    ~~~~~~~~~~~
    Django URL routes related to tracks.

    Copyright (C) 2015 FollowToDownload
"""
from django.conf.urls import patterns, url

from tracks import views


urlpatterns = patterns('',
    url(r'^upload', views.UploadView.as_view(), name='tracks.upload'),
    url(r'^info/(?P<track_id>.*)', views.InfoView.as_view(), name='tracks.info')
)
