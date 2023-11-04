from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_-]+$',
                message='Name must consist of letters, numbers, hyphens, and underscores only.',
            ),
        ],
    )
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, to_field='name', null=True)

    def __str__(self):
        return self.name
