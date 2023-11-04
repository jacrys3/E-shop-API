from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from e_shop.models import Product, Category


class ListProductsViewTestCase(TestCase):
    def setUp(self):
        """Create the client and products for testing GET requests to ProductView."""
        self.client = APIClient()
        self.product1 = Product.objects.create(
            name='New Product 1',
            description='Test1',
            price=1.00,
            category=None,
        )
        self.product2 = Product.objects.create(
            name='New Product 2',
            description='Test2',
            price=2.00,
            category=None,
        )

    def test_list_products_success(self):
        """Verifies that a GET request to ProductView successfully returns all products."""
        response = self.client.get('/api/products/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = [
            {
                'id': self.product1.id,
                'name': self.product1.name,
                'description': self.product1.description,
                'price': '1.00',
                'category': self.product1.category,
            },
            {
                'id': self.product2.id,
                'name': self.product2.name,
                'description': self.product2.description,
                'price': '2.00',
                'category': self.product2.category,
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
        self.assertEqual(product_data.name, create_data['name'])
        self.assertEqual(product_data.description, create_data['description'])
        self.assertEqual(float(product_data.price), float(create_data['price']))
        self.assertEqual(product_data.category, create_data['category'])

    def test_create_product_failure(self):
        """Verifies that a POST request to ProductView fails when bad input is given."""
        create_data = {
            'name': '',
        }
        response = self.client.post('/api/products/', create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)


class ListProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and product for testing GET requests to ChangeProductView."""
        self.client = APIClient()
        self.product = Product.objects.create(
            name='New Product',
            description='Test',
            price=10.00,
            category=None,
        )

    def test_list_product_success(self):
        """Verifies that a GET request to ChangeProductView successfully lists a product."""
        product_id = self.product.id

        response = self.client.get(f'/api/products/{product_id}/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = {
            'id': product_id,
            'name': self.product.name,
            'description': self.product.description,
            'price': '10.00',
            'category': self.product.category,
        }

        self.assertEqual(response_data, product_data)


class UpdateProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and product for testing PUT requests to ChangeProductView."""
        self.client = APIClient()
        self.product = Product.objects.create(
            name='New Product',
            description='Test',
            price=10.00,
            category=None,
        )

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
            'name': update_data['name'],
            'description': update_data['description'],
            'price': update_data['price'],
            'category': update_data['category'],
        }

        self.assertEqual(response_data, product_data)


class DeleteProductViewTestCase(TestCase):
    def setUp(self):
        """Create the client and product for testing DELETE requests to ChangeProductView."""
        self.client = APIClient()
        self.product = Product.objects.create(
            name='New Product',
            description='Test',
            price=10.00,
            category=None,
        )

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


class ListProductsByCategoryViewTestCase(TestCase):
    def setUp(self):
        """Create the client, product, and category for testing
            GET requests to ProductsByCategoryView"""
        self.client = APIClient()
        self.cat = Category.objects.create(
            name='Category',
            description='Test',
        )
        self.product = Product.objects.create(
            name='Product',
            description='Test',
            price=10.00,
            category=self.cat,
        )

    def test_list_products_by_category_success(self):
        """Verifies that a GET request to ProductsByCategoryView successfully
            returns all products of a specified category."""
        response = self.client.get(f'/api/products/category/{self.cat.name}/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = [{
            'id': self.product.id,
            'name': self.product.name,
            'description': self.product.description,
            'price': '10.00',
            'category': 'Category',
        }]

        self.assertEqual(len(response_data), len(product_data))

        self.assertEqual(response_data[0], product_data[0])

    def test_list_products_by_category_missing(self):
        """Verifies that a GET request to ProductsByCategoryView successfully
            returns no products when the category doesn't exist."""
        cat_name = 'Fake-Category'

        response = self.client.get(f'/api/products/category/{cat_name}/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response_data), 0)


class ListCategoriesViewTestCase(TestCase):
    def setUp(self):
        """Create the client and categories for testing GET requests to CategoryView."""
        self.client = APIClient()
        self.cat1 = Category.objects.create(
            name='Category1',
            description='Test1',
        )
        self.cat2 = Category.objects.create(
            name='Category2',
            description='Test2',
        )

    def test_list_categories_success(self):
        """Verifies that a GET request to CategoryView successfully returns all categories."""
        response = self.client.get('/api/category/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cat_data = [
            {
                'id': self.cat1.id,
                'name': self.cat1.name,
                'description': self.cat1.description,
            },
            {
                'id': self.cat2.id,
                'name': self.cat2.name,
                'description': self.cat2.description,
            }
        ]

        self.assertEqual(len(response_data), len(cat_data))

        self.assertEqual(response_data[0], cat_data[0])
        self.assertEqual(response_data[1], cat_data[1])


class CreateCategoryViewTestCase(TestCase):
    def setUp(self):
        """Create the client for testing POST requests to CategoryView."""
        self.client = APIClient()

    def test_create_category_success(self):
        """Verifies that a POST request to CategoryView
            creates a category with correct attributes."""

        create_data = {
            'name': 'New-Category',
            'description': 'Test',
        }

        response = self.client.post('/api/category/', create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Category.objects.count(), 1)

        cat_data = Category.objects.get()

        self.assertEqual(cat_data.id, 1)
        self.assertEqual(cat_data.name, create_data['name'])
        self.assertEqual(cat_data.description, create_data['description'])

    def test_create_category_failure(self):
        """Verifies that a POST request to CategoryView fails when bad input is given."""
        # name needs to be url-friendly
        create_data = {
            'name': 'New Category',
        }
        response = self.client.post('/api/category/', create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 0)


class ListCategoryViewTestCase(TestCase):
    def setUp(self):
        """Create the client and category for testing GET requests to ChangeCategoryView."""
        self.client = APIClient()
        self.cat = Category.objects.create(
            name='New-Category',
            description='Test',
        )

    def test_list_category_success(self):
        """Verifies that a GET request to ChangeCategoryView successfully lists a category."""
        cat_name = self.cat.name

        response = self.client.get(f'/api/category/{cat_name}/')

        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cat_data = {
            'id': self.cat.id,
            'name': self.cat.name,
            'description': self.cat.description,
        }

        self.assertEqual(response_data, cat_data)


class UpdateCategoryViewTestCase(TestCase):
    def setUp(self):
        """Create the client and category for testing PUT requests to ChangeCategoryView."""
        self.client = APIClient()
        self.cat = Category.objects.create(
            name='New-Category',
            description='Test',
        )

    def test_update_category_success(self):
        """Verifies that a PUT request to ChangeCategoryView successfully updates a category."""
        cat_name = self.cat.name

        update_data = {
            'name': 'Updated-Category',
            'description': 'Updated Test',
        }

        response = self.client.put(f'/api/category/{cat_name}/', update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.data

        cat_data = {
            'id': self.cat.id,
            'name': update_data['name'],
            'description': update_data['description'],
        }

        self.assertEqual(response_data, cat_data)


class DeleteCategoryViewTestCase(TestCase):
    def setUp(self):
        """Create the client and category for testing DELETE requests to ChangeCategoryView."""
        self.client = APIClient()
        self.cat = Category.objects.create(
            name='New-Category',
            description='Test',
        )

    def test_delete_category_success(self):
        """Verifies that a DELETE request to ChangeCategoryView successfully deletes a category."""
        cat_name = self.cat.name

        response = self.client.delete(f'/api/category/{cat_name}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Category.objects.count(), 0)

    def test_delete_category_fail(self):
        """Verifies that a DELETE request to ChangeCategoryView"""

        # name that is NOT connected to a Category
        cat_name = 'Fake-Category'

        response = self.client.delete(f'/api/category/{cat_name}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
