from django.shortcuts import render
from .models import Donation_opt
from django.views.generic import ListView


# Create your views here.
class Donation_optView(ListView):
    model = Donation_opt
