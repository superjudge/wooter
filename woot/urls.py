# -*- coding: utf-8 -*-

# Copyright (c) 2009, Johan Liseborn <johan.liseborn@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'woot.views.start', name='start'),
    url(r'^home/$', 'woot.views.home', name='home'),
    url(r'^following/$', 'woot.views.following', name='following'),
    url(r'^followers/$', 'woot.views.followers', name='followers'),
    url(r'^settings/$', 'woot.views.settings', name='settings'),
    url(r'^accounts/signup/$', 'woot.views.signup', name='signup'),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/(.*)', admin.site.root),

    # Use Django's built in login/logout
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/'}, name='logout'),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', name='change'),
    url(r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done', name='change-done'),
    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset'),
    url(r'^accounts/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='reset-done'),

#    (r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^(?P<username>\w+)/$', 'woot.views.profile', name='user-profile'),
    url(r'^(?P<username>\w+)/following/$', 'woot.views.following', name='user-following'),
    url(r'^(?P<username>\w+)/followers/$', 'woot.views.followers', name='user-followers'),
    url(r'^(?P<username>\w+)/follow/$', 'woot.views.follow', name='user-follow'),
    url(r'^(?P<username>\w+)/unfollow/$', 'woot.views.unfollow', name='user-unfollow'),
)

if settings.DEBUG:
    import os.path
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/'), 'show_indexes': True}),
    )
