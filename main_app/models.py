from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/')


class SizeQuantity(models.Model):
    product = models.ForeignKey('Product', related_name='sizes_and_quantities', on_delete=models.CASCADE)
    size_choices = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    size = models.CharField(max_length=2, choices=size_choices)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.get_size_display()} - {self.quantity} available"


class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    composition = models.TextField()

    def __str__(self):
        return self.name