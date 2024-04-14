from django.contrib import admin

# Register your models here.
from .models import Employee, Offer, Product

admin.site.register(Employee)
admin.site.register(Offer)
admin.site.register(Product)
