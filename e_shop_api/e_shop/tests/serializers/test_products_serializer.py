from django.test import TestCase
from e_shop.models import Product, Category
from e_shop.serializers import ProductSerializer, CategorySerializer


class ProductSerializerTest(TestCase):
    def test_serializer_output(self):
        """Verifies that the output from ProductSerializer is correct."""
        product_data = {
            'name': 'Sample Product',
            'description': 'A sample product description',
            'price': '19.99',
            'category': None,
        }
        product = Product(**product_data)

        serializer = ProductSerializer(product)
        serialized_data = serializer.data

        self.assertEqual(
            serialized_data,
            {
                'id': None,
                'name': 'Sample Product',
                'description': 'A sample product description',
                'price': '19.99',
                'category': None,
            }
        )


class CategorySerializerTest(TestCase):
    def test_serializer_output(self):
        """Verifies that the output from CategorySerializer is correct."""
        cat_data = {
            'name': 'Test-Category',
            'description': 'Test',
        }
        category = Category(**cat_data)

        serializer = CategorySerializer(category)
        serialized_data = serializer.data

        self.assertEqual(
            serialized_data,
            {
                'id': None,
                'name': 'Test-Category',
                'description': 'Test',
            }
        )
