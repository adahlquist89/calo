from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CaloUserManager(BaseUserManager):
	def create_user(self, email=None, first_name=None, last_name=None, date_of_birth=None, password=None, username=None):
		if not email:
			raise ValueError('Email is required!')

		user = self.model(
				email=CaloUserManager.normalize_email(email),
				first_name=first_name,
				last_name=last_name,
			   )

		user.set_password(password)
		user.save(using=self._db)
		user_profile = Profile(user=user)
		user_profile.save()

		return user

	def create_superuser(self, email, first_name, last_name, date_of_birth, password):
		user = self.create_user(email, first_name, last_name, date_of_birth, password)
		user.is_admin = True
		user.is_active = True
		user.save(using=self._db)

		return user

class CaloUser(AbstractBaseUser):
	email = models.EmailField(
				verbose_name='Email address',
				max_length=255,
				unique=True,
			)
	first_name = models.CharField(
					verbose_name='First name',
					max_length=32,
					db_index=True,
				)
	last_name = models.CharField(
					verbose_name='Last name',
					max_length=32,
					db_index=True,
				)

	friends = models.ManyToManyField("self",symmetrical=False)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = CaloUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def get_full_name(self):
		"""Representacion completa de un usuario."""
		return self.first_name + ' ' + self.last_name

	def get_short_name(self):
		"""Representacion abreviada de un usuario."""
		return self.email

	def __unicode__(self):
		return self.get_full_name()

	def has_perm(self, perm, obj=None):
		"""Permisos especificos de usuario, por ahora siempre true."""
		return True

	def has_module_perms(self, app_label):
		"""Permisos para un modulo determinado, por ahora siempre true."""
		return True

	@property
	def is_staff(self):
		return self.is_admin

class Profile(models.Model):
	
	NACIONALITY_CHOICES = (
		('AR', 'Argentina'),
		('BR', 'Brasil'),
		('UR', 'Uruguay'), #etc
	)

	user = models.OneToOneField('CaloUser')
	friends = models.
	nacionality = models.CharField(max_length=2, choices=NACIONALITY_CHOICES, default='AR')