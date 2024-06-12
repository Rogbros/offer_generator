from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from utils.mixins import HTMXSwapPartialMixin
from utils.mixins import HTMXRedirectMixin
from django.utils.decorators import method_decorator
from allauth.account.decorators import login_required


class HTMXListView(HTMXSwapPartialMixin, ListView):
    template_name = None
    partial_template_name = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class HTMXCreateView(HTMXRedirectMixin, CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class HTMXUpdateView(HTMXRedirectMixin, UpdateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class HTMXDeleteView(HTMXSwapPartialMixin, DeleteView):
    partial_template_name = "products/partials/products_list_table.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
