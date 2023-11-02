from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from e_shop.models import Product


class ListProductsViewTestCase(TestCase):
    def setUp(self):
        """Create the client and products for testing GET requests to ProductView."""
        self.client = APIClient()
        self.product1 = Product.objects.create(name='New Product 1', description='Test1', price=1.00, category=None)
        self.product2 = Product.objects.create(name='New Product 2', description='Test2', price=2.00, category=None)

    def test_list_product_success(self):
        """Verifies that a GET request to ProductView successfully returns all products."""
        response = self.client.get('/api/products/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = [
            {
                'id': self.product1.id,
                'name': 'New Product 1',
                'description': 'Test1',
                'price': '1.00',
                'category': None,
            },
            {
                'id': self.product2.id,
                'name': 'New Product 2',
                'description': 'Test2',
                'price': '2.00',
                'category': None,
            }
        ]

        self.assertEqual(len(response_data), len(product_data))

        self.assertEqual(response_data[0], product_data[0])
        self.assertEqual(response_data[1], product_data[1])


class CreateProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client for testing POST requests to ProductView."""
        self.client = APIClient()

    def test_create_product_success(self):
        """Verifies that a POST request to ProductView creates a product with correct attributes."""

        create_data = {
            'name': 'New Product',
            'description': 'A new product description',
            'price': '29.99',
            'category': None,
        }

        response = self.client.post('/api/products/', create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Product.objects.count(), 1)

        product_data = Product.objects.get()

        self.assertEqual(product_data.id, 1)
        self.assertEqual(product_data.name, 'New Product')
        self.assertEqual(product_data.description, 'A new product description')
        self.assertEqual(float(product_data.price), 29.99)
        self.assertEqual(product_data.category, None)

    def test_create_product_failure(self):
        """Verifies that a POST request to ProductView fails when bad input is given."""
        create_data = {
            'name': '',
        }
        response = self.client.post('/api/products/', create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)


# class ListProductViewTestCase(TestCase):


class UpdateProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and product for testing PUT requests to ChangeProductView."""
        self.client = APIClient()
        self.product = Product.objects.create(name='New Product', description='Test', price=10.00, category=None)

    def test_update_product_success(self):
        """Verifies that a PUT request to ChangeProductView successfully updates a product."""
        product_id = self.product.id

        update_data = {
            'name': 'Updated Product',
            'description': 'Updated Test',
            'price': '11.00',
            'category': None,
        }

        response = self.client.put(f'/api/products/{product_id}/', update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.data

        product_data = {
            'id': product_id,
            'name': 'Updated Product',
            'description': 'Updated Test',
            'price': '11.00',
            'category': None,
        }

        self.assertEqual(response_data, product_data)


class DeleteProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and product for testing DELETE requests to ChangeProductView."""
        self.client = APIClient()
        self.product = Product.objects.create(name='New Product', description='Test', price=10.00, category=None)

    def test_delete_product_success(self):
        """Verifies that a DELETE request to ChangeProductView successfully deletes a product."""
        product_id = self.product.id

        response = self.client.delete(f'/api/products/{product_id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Product.objects.count(), 0)

    def test_delete_product_fail(self):
        """Verifies that a DELETE request to ChangeProductView"""

        # id that is NOT connected to a Product
        product_id = 999

        response = self.client.delete(f'/api/products/{product_id}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
