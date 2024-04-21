from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "offers/pages/main.html"


class OffersView(TemplateView):
    template_name = "offers/pages/offer_view.html"
