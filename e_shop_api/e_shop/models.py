from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    # need to authenticate!
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Product(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.CharField(max_length=30)

# look into maybe creating orderItem?
class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )

    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default='pending', max_length=20)
    total_cost = models.DecimalField(decimal_places=2, max_digits=15)

# look into maybe creating cartItem?
class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)