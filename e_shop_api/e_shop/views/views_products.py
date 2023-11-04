from rest_framework import generics
from e_shop.models import Product, Category
from e_shop.serializers import ProductSerializer, CategorySerializer


class ProductView(generics.ListCreateAPIView):
    """
    List and create products.

    This view allows you to list all existing products with a GET request
    and create new products with a POST request.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ChangeProductView(generics.RetrieveUpdateDestroyAPIView):
    """
    List, update and delete a single product.

    This view allows you to list the current product with a GET request,
    update the existing product with a PUT request,
    and delete the existing product with a DELETE request.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsByCategoryView(generics.ListAPIView):
    """
    List products by category.

    This view allows you to list all products in a single category with a GET request.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Product.objects.filter(category=category_name)


class CategoryView(generics.ListCreateAPIView):
    """
    List and create categories.

    This view allows you to list all existing categories with a GET request
    and create new categories with a POST request.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChangeCategoryView(generics.RetrieveUpdateDestroyAPIView):
    """
    List, update and delete a single category.

    This view allows you to list the current category with a GET request,
    update the existing category with a PUT request,
    and delete the existing category with a DELETE request.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
