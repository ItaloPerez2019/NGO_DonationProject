from django.db import models
from django.urls import reverse


class User(models.Model):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.CharField(max_length=250, unique=True)
	role = models.CharField(max_length=250)

	def __str__(self):
		return '{}'.format(self.email)

	def get_absolute_url(self):
		return reverse('user-list')
