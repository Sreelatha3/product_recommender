from django.core.management.base import BaseCommand
from orders.models import Order
from products.models import Product
import random

class Command(BaseCommand):
    help = "Generate sample orders with random products"

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.ERROR(" No products found. Please run generate_products first."))
            return

        for _ in range(30):  # Create 30 sample orders
            order = Order.objects.create()
            num_products = random.randint(2, 5)
            selected_products = random.sample(products, num_products)
            order.products.set(selected_products)
        self.stdout.write(self.style.SUCCESS(" Successfully generated sample orders."))
