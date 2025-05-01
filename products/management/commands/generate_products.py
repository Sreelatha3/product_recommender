from django.core.management.base import BaseCommand
from products.models import Product
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        for i in range(20):
            Product.objects.create(
                name=f"Product {i}",
                category=random.choice(["Electronics", "Books", "Clothing"]),
                price=random.uniform(2000, 50000),
                description="Auto generated product"
            )
