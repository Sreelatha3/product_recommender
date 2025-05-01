from itertools import combinations
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # Get all orders
    serializer_class = OrderSerializer  # Use the OrderSerializer
   
from django.shortcuts import render
from django.db.models import Count
from .models import Order

# views.py
from django.shortcuts import render
from .models import Order
from collections import Counter
from products.models import Product

def frequently_bought_together_dashboard(request):
    # Fetch orders and their products
    orders = Order.objects.prefetch_related('products').all()
    
    # Collect all product combinations bought together
    product_combinations = []
    for order in orders:
        products = order.products.all()
        product_combinations.extend(combinations(products, 2))  # Get all pairs of products in an order

    # Count frequency of product combinations
    product_pair_counts = Counter(product_combinations)
    
    # Prepare a list of most frequently bought pairs
    frequent_pairs = []
    for (product1, product2), count in product_pair_counts.most_common(10):  # Get top 10 pairs
        frequent_pairs.append({
            'product1': product1,
            'product2': product2,
            'count': count
        })

    # Pass the data to the template
    return render(request, 'orders/dashboard.html', {'frequent_pairs': frequent_pairs})
