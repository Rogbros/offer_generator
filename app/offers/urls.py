from django.urls import path

from offers.views.offers import OffersView
from offers.views.offers import MainView

app_name = "offers"
urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("offers", OffersView.as_view(), name="offers"),
]
