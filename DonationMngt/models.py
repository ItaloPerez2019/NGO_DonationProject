from django.db import models
from django.urls import reverse
import datetime

class Donation(models.Model):
	name = models.CharField(max_length=250)
	date = models.DateField(default=datetime.date.today)
	amount = models.DecimalField(max_digits=20, decimal_places=2)
	donation_type = models.CharField(max_length=250)

	def __str__(self):
		return '{}'.format(self.name)

	def get_absolute_url(self):
		return reverse('donation-list')
