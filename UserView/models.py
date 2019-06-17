from django.db import models
from django.urls import reverse


class Donation_opt(models.Model):
		first_name = models.CharField(max_length=250)
		last_name = models.CharField(max_length=250)
		cma = models.CharField(max_length=250)
		phone = models.CharField(max_length=20)
		emailaddress = models.CharField(max_length=250, unique=True)
		address_1 = models.CharField(max_length=100)
		address_2 = models.CharField( max_length=100)
		city = models.CharField( max_length=50)
		state = models.CharField(max_length=50)
		zipcode = models.CharField(max_length=10)
		country = models.CharField( max_length=50)
		urbanization = models.CharField( max_length=50)

		def __str__(self):
			return '{}'.format(self.cma)

		def get_absolute_url(self):
			return reverse('donation_opt-list')
