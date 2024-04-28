from django.views.generic import TemplateView
from .general import HTMXListView


class MainView(TemplateView):
    template_name = "offers/pages/main.html"


class OffersView(HTMXListView):
    template_name = "offers/pages/offer_view.html"
    partial_template_name = ""
