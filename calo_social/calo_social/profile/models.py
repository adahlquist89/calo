from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Profile(models.Model):
    
    

    """Main Profile Object - Holds extra profile data retrieved from auth providers"""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, related_name="profile", verbose_name=_("Profile"))
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES, verbose_name=_("Gender"))
    image_url = models.URLField(blank=True, verbose_name=_("Avatar Picture"))
    description = models.TextField(blank=True, verbose_name=_("Description"), help_text=_("Tell us about yourself!"))

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ['user__username']

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return 'profile_other_view_page', [self.user.username]


