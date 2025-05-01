# Product Recommender System (Django + DRF)
This project is a Product Recommendation System built using Django and Django REST Framework. It supports CRUD APIs for managing products and orders, and implements a simple recommendation logic based on frequently bought together items.

# Assumptions 
1. Frequently bought together is based on orders containing multiple products.
2. Recommendations are generated using collaborative filtering.
3. Orders model or table has Many-to-Many relation, as one order can have multiple products.
4. Using the ModelViewSet class instead of manually defining the CRUD APIS.

# Development
1. Created models for products and orders
2. Defined scripts to populate random products and orders.
3. CRUD API's to handles operations like create, read , update , delete.
4. Created an API that accepts product ids and returns the recommendations.
5. Created a dashboard to see the frequently bought products ( Brownie points)
http://127.0.0.1:8000/api/orders/dashboard/frequently-bought-together/



