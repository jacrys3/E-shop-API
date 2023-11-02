from django.test import TestCase
from rest_framework.test import APIClient
from e_shop.models import Product

class CreateProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and data for testing CreateProductView."""
        self.client = APIClient()

    def test_create_product_success(self):
        """Tests that the create_product view properly creates a product with correct attributes."""

        valid_data = {
            'name': 'New Product',
            'description': 'A new product description',
            'price': '29.99',
        }
        response = self.client.post('/api/create-product/', valid_data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'New Product')
        self.assertEqual(Product.objects.get().description, 'A new product description')
        self.assertEqual(float(Product.objects.get().price), 29.99)

    def test_create_product_failure(self):
        """Tests that the create_product view properly fails when bad input is given."""
        invalid_data = {
            'name': '',
        }
        response = self.client.post('/api/create-product/', invalid_data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Product.objects.count(), 0)