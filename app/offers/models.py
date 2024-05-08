from django.db import models
import uuid

# Create your models here.


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    email = models.EmailField(max_length=200, unique=False)
    photo = models.ImageField(upload_to="employees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=False)
    type = models.CharField(max_length=200, unique=False)
    size = models.CharField(max_length=200, unique=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    products = models.ManyToManyField(Product)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
