from django.urls import path
from e_shop.views.views_products import (
    ProductView,
    ChangeProductView,
    ProductsByCategoryView,
    CategoryView,
    ChangeCategoryView,
)

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('products/<int:pk>/', ChangeProductView.as_view(), name='change-product'),
    path(
        'products/category/<str:category_name>/',
        ProductsByCategoryView.as_view(),
        name='product-by-category'
    ),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<str:name>/', ChangeCategoryView.as_view(), name='change-category'),
]
