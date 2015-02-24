from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

import follow.urls
import tracks.urls
import users.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'f2d.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'f2d.views.homepage', name='homepage'),
    url(r'^d/', include(follow.urls)),
    url(r'^tracks/', include(tracks.urls)),
    url(r'^users/', include(users.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}))
