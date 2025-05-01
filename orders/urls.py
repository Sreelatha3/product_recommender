from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet,frequently_bought_together_dashboard


router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path("dashboard/frequently-bought-together/", frequently_bought_together_dashboard, name="fbt_dashboard"),
]