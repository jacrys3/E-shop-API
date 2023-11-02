from django.test import TestCase
from e_shop.models import Product
from e_shop.serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def test_serializer_output(self):
        """Verifies that the output from ProductSerializer is correct."""
        # Create a sample Product instance
        product_data = {
            'name': 'Sample Product',
            'description': 'A sample product description',
            'price': '19.99',
            'image': 'sample.jpg',
        }
        product = Product(**product_data)
        
        # Serialize the Product instance
        serializer = ProductSerializer(product)
        serialized_data = serializer.data
        
        # Verify the serialized data
        self.assertEqual(
            serialized_data,
            {
                'name': 'Sample Product',
                'description': 'A sample product description',
                'price': '19.99',
                'image': 'sample.jpg',
            }
        )