"""
    f2d.views
    ~~~~~~~~~
    Django views not categorizable under any other module.

    Copyright (C) 2015 FollowToDownload
"""
from django.shortcuts import render


def homepage(request):
    """Render the landing page of the website."""
    context = {'is_homepage': True}
    return render(request, 'f2d/homepage.html', context) 
