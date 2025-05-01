from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product
from orders.models import Order
from .serializers import ProductSerializer
from collections import Counter
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Get all products
    serializer_class = ProductSerializer  # Use the ProductSerializer

    @action(detail=True, methods=['get'], url_path='recommendations')
    def recommend_products(self, request, pk=None):
        try:
            # Fetch the current product by pk (automatically handled by get_object())
            product = self.get_object()
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        # Get all orders that contain this product
        orders_with_product = Order.objects.filter(products=product)

        # Collect all other products from those orders
        co_purchased_products = []
        for order in orders_with_product:
            # Exclude the current product from being recommended
            for p in order.products.exclude(id=product.id):
                co_purchased_products.append(p)

        # Count the frequency of co-purchased products
        product_counts = Counter(co_purchased_products)
        
        # Get the top 5 most frequent co-purchased products
        top_recommendations = [prod for prod, _ in product_counts.most_common(5)]

        # Serialize and return the recommended products
        serializer = ProductSerializer(top_recommendations, many=True)
        return Response(serializer.data)