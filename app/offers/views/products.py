from .general import HTMXListView
from offers.models import Product


class ProductsView(HTMXListView):
    template_name = "products/pages/products_list.html"
    partial_template_name = ""
    context_object_name = "products"

    queryset = Product.objects.all()
