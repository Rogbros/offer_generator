from django.urls import path

from offers.views.offers import OffersView
from offers.views.offers import MainView
from offers.views.products import ProductsView
from offers.views.products import CreateProductView

app_name = "offers"
urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("offers", OffersView.as_view(), name="offers"),
    path("products", ProductsView.as_view(), name="products"),
    path("products/create", CreateProductView.as_view(), name="create_product"),
]
