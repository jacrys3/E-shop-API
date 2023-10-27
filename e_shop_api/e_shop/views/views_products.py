from rest_framework import generics
from e_shop.models import Product
from e_shop.serializers import ProductSerializer

class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer