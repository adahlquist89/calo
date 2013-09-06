from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
from social_auth.backends.google import GoogleOAuth2Backend
from social_auth.signals import socialauth_registered, pre_update


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)



@receiver(socialauth_registered, sender=GoogleOAuth2Backend)
def google_extra_values(sender, user, response, details, **kwargs):
    """Populates a UserProfile Object when a new User is created via Google Auth"""
    LOGGER.debug('profile.models.google_extra_values')
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    data = {'access_token': response.get('access_token', ''), 'alt': 'json'}
    params = urlencode(data)
    try:
        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
        result = simplejson.loads(urlopen(request).read())

        user.last_name = result.get('family_name', '')
        user.first_name = result.get('given_name', '')
        profile = user.profile
        profile.gender = result.get('gender', '')
        profile.image_url = result.get('picture', '')
        profile.url = result.get('link', '')

        profile.save()
    except:
        pass

    return True

socialauth_registered.connect(google_extra_values, sender=GoogleOAuth2Backend)



