from django.urls import path

from offers.views import OffersView

app_name = "offers"
urlpatterns = [
    path("", OffersView.as_view(), name="offers"),
]
