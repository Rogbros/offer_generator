from .general import HTMXListView
from .general import HTMXCreateView
from .general import HTMXUpdateView
from offers.models import Product
from offers.forms.products import NewProductForm


class ProductsView(HTMXListView):
    template_name = "products/pages/products_list.html"
    partial_template_name = "products/partials/products_list_table.html"
    context_object_name = "products"

    ordering = ["-created_at"]

    queryset = Product.objects.all()


class CreateProductView(HTMXCreateView):
    template_name = "products/pages/new_product.html"
    partial_template_name = "products/forms/new_product_form.html"
    form_class = NewProductForm
    success_url = "/products"
    pass_request_to_form = True

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProductView(HTMXUpdateView):
    template_name = "products/pages/update_product.html"
    partial_template_name = "products/forms/update_product_form.html"
    form_class = NewProductForm
    success_url = "/products"
    pass_request_to_form = True
    context_object_name = "product"

    def get_object(self):
        return Product.objects.get(id=self.kwargs.get("id"))


class DeleteProductView(HTMXUpdateView):
    template_name = "products/pages/update_product.html"
    partial_template_name = "products/forms/update_product_form.html"
    form_class = NewProductForm
    success_url = "/products"
    pass_request_to_form = True
    context_object_name = "product"

    def get_object(self):
        return Product.objects.get(id=self.kwargs.get("id"))
