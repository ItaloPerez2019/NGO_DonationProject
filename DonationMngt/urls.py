from django.urls import path
from .views import DonationListView

urlpatterns = [
    path('', DonationListView.as_view(), name='donation-list'),
]
