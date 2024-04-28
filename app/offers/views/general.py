from django.views.generic import ListView
from utils.mixins import HTMXSwapPartialMixin
from django.utils.decorators import method_decorator
from allauth.account.decorators import login_required


class HTMXListView(HTMXSwapPartialMixin, ListView):
    template_name = None
    partial_template_name = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
