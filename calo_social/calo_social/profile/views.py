"""Django Views for the profile"""

# pylint: disable=R0901

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
from models import Profile
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _

from forms import ProfileForm

import logging

LOGGER = logging.getLogger(name='profile')

DEFAULT_RETURNTO_PATH = getattr(settings, 'DEFAULT_RETURNTO_PATH', '/')


class ProfileView(FormView):
    """
    Profile View Page

    url: /profile/view
    """
    template_name = 'profile/profile_view.html'

    form_class = ProfileForm #Profile Form in profile/forms.py

    http_method_names = ['get'] #Limit to 'get' for security reasons

    def get_initial(self):
        """Load up the default data to show in the display form."""
        LOGGER.debug("profile.views.ProfileView.get_initial")
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
        elif self.request.user.is_authenticated():
            user = self.request.user
        else:
            raise Http404 #Case where user gets to this view anonymously for non-existent user

        returnTo = self.request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)

        profile = Profile.objects.get(user=user) #Get user Profile

        self.object = profile

        initial_data = model_to_dict(profile)
        initial_data.update(model_to_dict(user))
        initial_data.update({'returnTo': returnTo})

        return initial_data


class ProfileEditView(UpdateView):
    """
    Profile Editing View

    url: /profile/edit
    """

    template_name = 'profile/profile_edit.html'

    form_class = ProfileForm

    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user) #Force get from current user for security

    def get_initial(self):
        """Load up the default data to show in the form."""
        LOGGER.debug("profile.views.ProfileEditView.get_initial")

        returnTo = self.request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)
        self.success_url = returnTo

        initial_data = self.initial.copy() #Copy data loaded automatically to start with
        initial_data.update(model_to_dict(self.request.user)) # Add current user data
        initial_data.update({'returnTo': returnTo})

        return initial_data

    def form_valid(self, form):
        """ Update OK """
        messages.add_message(self.request, messages.INFO, _('Your profile has been updated.'))
        self.success_url = form.cleaned_data.get('returnTo')
        return super(ProfileEditView, self).form_valid(form)

    def form_invalid(self, form):
        """ Update KO """
        messages.add_message(self.request, messages.INFO, _('Your profile has NOT been updated.'))
        return super(ProfileEditView, self).form_invalid(form)


