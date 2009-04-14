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

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ungettext

from woot.forms import WootForm, SignupForm
from woot.models import Woot, Profile

# ---------------------------------------------------------------------
def start(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        return render_to_response('woot/start.html')

# ---------------------------------------------------------------------
@login_required
def home(request):
    profile = request.user.get_profile()
    
    if request.method == 'POST':
        form = WootForm(request.POST)
        
        if form.is_valid():
            Woot.objects.create(user=profile, text=form.cleaned_data['text'])

            return HttpResponseRedirect(reverse('home'))

    else:
        form = WootForm()
        
    # look up all the woots in the users time line (his own and all of the users he is following)
    woots = Woot.objects.filter(Q(user=profile) | Q(user__followers=profile)).distinct()

    return render_to_response('woot/home.html', {'form':form, 'woots':woots}, context_instance=RequestContext(request))
    
# ---------------------------------------------------------------------
def profile(request, username):
    profile = get_object_or_404(User, username=username).get_profile()
    woots = Woot.objects.filter(user=profile)
    
    return render_to_response('woot/profile.html', {'profile':profile, 'woots':woots}, context_instance=RequestContext(request))

# ---------------------------------------------------------------------
def followers(request, username=None):
    user = request.user if username is None else get_object_or_404(User, username=username)
            
    return render_to_response('woot/followers.html', {'profile':user.get_profile(), 'followers':user.get_profile().followers.all()}, context_instance=RequestContext(request))

# ---------------------------------------------------------------------
def following(request, username=None):
    user = request.user if username is None else get_object_or_404(User, username=username)
        
    return render_to_response('woot/following.html', {'profile':user.get_profile(), 'following':user.get_profile().following.all()}, context_instance=RequestContext(request))

# ---------------------------------------------------------------------
def follow(request, username):
    pass

# ---------------------------------------------------------------------
def unfollow(request, username):
    pass

# ---------------------------------------------------------------------
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            Profile.objects.create(user=user)

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)

            return HttpResponseRedirect(reverse('home'))

    else:
        form = SignupForm()

    return render_to_response('woot/signup.html', {'form':form}, context_instance=RequestContext(request))

# ---------------------------------------------------------------------
@login_required
def settings(request):
    pass
