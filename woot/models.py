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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

LANGUAGE_CHOICES = (('SV', _('Swedish')), ('EN', _('English')))

# ---------------------------------------------------------------------
class Profile(models.Model):
    "The user profile."

    user = models.ForeignKey(User, verbose_name=_(u'User'), unique=True)

    following = models.ManyToManyField('self',
                                       verbose_name=_(u'Following'),
                                       symmetrical=False,
                                       related_name='followers',
                                       blank=True,
                                       null=True,
                                       help_text=_(u'The other users this user is following.'))

    url = models.URLField(_(u'More info URL'),
                          blank=True,
                          help_text=_(u'A URL pointing to additional information about the user.'))

    bio = models.CharField(_(u'One line bio'),
                           blank=True,
                           max_length=160,
                           help_text=_(u'A one line bio for the user.'))

    location = models.CharField(_(u'Location'),
                                blank=True,
                                max_length=100,
                                help_text=_(u'The users physical location, e.g. hometown.'))

    language = models.CharField(_(u'Language'),
                                max_length=2,
                                choices=LANGUAGE_CHOICES,
                                default='sv',
                                help_text=_(u'The users preferred lanugage.'))

    public = models.BooleanField(_(u'Public'),
                                 default=True,
                                 help_text=_(u'Show woots on the public timeline, or only to followers.'))

    def __unicode__(self):
        return self.user.username
    
class ProfileInline(admin.TabularInline):
    model = Profile
    max_num = 1

class UserAndProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAndProfileAdmin)

# ---------------------------------------------------------------------
class Woot(models.Model):
    "A Wooter entry."
    
    user = models.ForeignKey(Profile,
                             verbose_name=_(u'User'),
                             related_name='woots',
                             help_text=_(u'The user who wrote the woot.'))

    timestamp = models.DateTimeField(_(u'Posted'),
                                     auto_now_add=True,
                                     editable=False,
                                     help_text=_(u'When the woot was posted.'))

    text = models.CharField(_(u'Text'),
                            max_length=140,
                            help_text=_(u'The actual woot, i.e. the posted text.'))

    class Meta:
        ordering = ['-timestamp']
        
    def __unicode__(self):
        return self.text

admin.site.register(Woot)
