from django.test import TestCase
from e_shop.models import Product


class ProductModelTests(TestCase):
    def test_product_creation(self):
        product = Product(
            name="Sample Product",
            description="A sample product description.",
            price=19.99,
            category=None  # Replace with an actual category if needed
        )

        product.save()

        saved_product = Product.objects.get(id=product.id)

        self.assertEqual(saved_product.name, "Sample Product")
        self.assertEqual(saved_product.description, "A sample product description.")
        self.assertEqual(float(saved_product.price), 19.99)
        self.assertIsNone(saved_product.category)

        product.delete()
