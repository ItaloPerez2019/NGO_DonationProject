from django.shortcuts import render
from . models import Donation
from django.views.generic import ListView


class DonationListView(ListView):
    model=Donation
