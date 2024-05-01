from .general import HTMXListView
from .general import HTMXCreateView
from offers.models import Product
from offers.forms.products import NewProductForm


class ProductsView(HTMXListView):
    template_name = "products/pages/products_list.html"
    partial_template_name = "products/partials/products_list_table.html"
    context_object_name = "products"

    queryset = Product.objects.all()


class CreateProductView(HTMXCreateView):
    template_name = "products/pages/new_product.html"
    partial_template_name = "products/forms/new_product_form.html"
    form_class = NewProductForm
    success_url = "/products/"
    pass_request_to_form = True
