"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614, E1120

from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from calo_social.profile.views import ProfileView
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    # Profile Self View
    url(r'^$', never_cache(ProfileView.as_view()), name="profile_view_page"),

    # Profile Other View
    url(r'^view/(?P<username>(\w+)(\.)*(\w)*)/$', ProfileView.as_view(), name="profile_other_view_page"),

)