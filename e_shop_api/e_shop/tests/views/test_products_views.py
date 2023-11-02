from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from e_shop.models import Product


class CreateProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client for testing CreateProductView."""
        self.client = APIClient()

    def test_create_product_success(self):
        """Verifies that a POST request to ProductView creates a product with correct attributes."""

        valid_data = {
            'name': 'New Product',
            'description': 'A new product description',
            'price': '29.99',
        }
        response = self.client.post('/api/products/', valid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'New Product')
        self.assertEqual(Product.objects.get().description, 'A new product description')
        self.assertEqual(float(Product.objects.get().price), 29.99)

    def test_create_product_failure(self):
        """Verifies that a POST request to ProductView fails when bad input is given."""
        invalid_data = {
            'name': '',
        }
        response = self.client.post('/api/products/', invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)


class ListProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and products for testing ListProductView."""
        self.client = APIClient()
        Product.objects.create(name='New Product', description='Test', price=10.00, category=None)

    def test_list_product_success(self):
        """Verifies that a GET request to ProductView successfully returns all products."""
        response = self.client.get('/api/products/')

        print(response.data) # check if data is correct

        self.assertEquals(response.status_code, status.HTTP_200_OK)
