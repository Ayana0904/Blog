from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=20)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)