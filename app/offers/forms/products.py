from django import forms
from offers.models import Product


class NewProductForm(forms.ModelForm):
    name = forms.CharField(required=True)
    type = forms.CharField(required=True)
    size = forms.CharField(required=False)
    price = forms.DecimalField(required=True)
    short_description = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.ImageField(required=True)

    class Meta:
        model = Product
        fields = ["name", "type", "size", "price", "short_description", "description", "image"]
