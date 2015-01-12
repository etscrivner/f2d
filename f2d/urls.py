from django.conf.urls import patterns, include, url
from django.contrib import admin

import tracks.urls
import users.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'f2d.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'f2d.views.homepage', name='homepage'),
    url(r'^tracks/', include(tracks.urls)),
    url(r'^users/', include(users.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
