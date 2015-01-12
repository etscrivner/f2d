"""
    users.admin
    ~~~~~~~~~~~
    Administrative interfaces for users.

    Copyright (C) 2015 FollowToDownload
"""
from django.contrib import admin

from users import models


class SoundCloudUserAdmin(admin.ModelAdmin):
    list_display = [
        'soundcloud_user_id',
        'soundcloud_id',
        'permalink',
        'username',
        'full_name'
    ]


admin.site.register(models.SoundCloudUser, SoundCloudUserAdmin)
