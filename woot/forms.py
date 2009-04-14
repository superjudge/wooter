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

from django import forms
from django.utils.translation import ugettext as _

class WootForm(forms.Form):
    text = forms.CharField(label=_(u'Text'), max_length=140, required=False, widget=forms.Textarea(attrs={'rows':2}))

class SignupForm(forms.Form):
    first_name = forms.CharField(label=_(u'First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_(u'Last name'), max_length=30, required=False)
    username = forms.CharField(label=_(u'Username'), max_length=30)
    password = forms.CharField(label=_(u'Password'), max_length=32, widget=forms.PasswordInput)
    email = forms.EmailField(label=_(u'email'))
    send_info = forms.BooleanField(label=_(u'Send me stuff'), required=False)
    
