from rest_framework.routers import DefaultRouter
from product.views import CategoryAPI, ProductAPI, PopulateProduct, ProductListInfo
from django.urls import path, include

router = DefaultRouter()
router.register("category", CategoryAPI, basename="category")
router.register("product", ProductAPI, basename="product")

urlpatterns = [
    path("api/", include(router.urls)),
    path("products/", PopulateProduct.as_view(), name="products"),
    path("product-list/", ProductListInfo.as_view(), name="product-list-info"),
]
