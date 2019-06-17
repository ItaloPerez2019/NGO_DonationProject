from django.urls import path
from .views import Donation_optView

urlpatterns = [
    path('', Donation_optView.as_view(), name='donation_opt-list'),
]
