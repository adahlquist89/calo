from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.OneToOneField(User, related_name="profile")
    #acá abajo van todos los datos extra que querramos poner en el profile
