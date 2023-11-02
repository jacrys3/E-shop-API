from django.urls import path
from e_shop.views.views_products import ProductView, ChangeProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('products/<int:pk>/', ChangeProductView.as_view(), name='delete-product'),
]
