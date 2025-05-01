from django.db import models
from products.models import Product

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders')

    def __str__(self):
        return f"Order #{self.id} - {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"