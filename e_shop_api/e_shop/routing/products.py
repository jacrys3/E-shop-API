from django.urls import path
from e_shop.views.views_products import ProductView, ProductChangeView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('products/<int:pk>/', ProductChangeView.as_view(), name='delete-product'),
]
