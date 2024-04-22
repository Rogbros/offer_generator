from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from allauth.account.decorators import login_required


class MainView(TemplateView):
    template_name = "offers/pages/main.html"


class OffersView(TemplateView):
    template_name = "offers/pages/offer_view.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
