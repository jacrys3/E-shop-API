from rest_framework import generics
from e_shop.models import Product
from e_shop.serializers import ProductSerializer


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
