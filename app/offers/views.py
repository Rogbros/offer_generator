from django.views.generic import TemplateView


class OffersView(TemplateView):
    template_name = "offers/pages/offer_view.html"
