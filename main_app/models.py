from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорiя"
        verbose_name_plural = "Додання категорiй"


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/', verbose_name="Фото")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class SizeQuantity(models.Model):
    product = models.ForeignKey('Product', related_name='sizes_and_quantities', on_delete=models.CASCADE)
    size_choices = [
        ('NS', 'No Size'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    size = models.CharField(max_length=2, choices=size_choices, default='NS', verbose_name="Розмір")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")

    def __str__(self):
        return f"{self.get_size_display()} - {self.quantity} available"

    class Meta:
        verbose_name = "Розмір"
        verbose_name_plural = "Розміри"

@receiver(post_save, sender=SizeQuantity)
def update_product_status(sender, instance, **kwargs):
    """
    Обновляет статус продукта в зависимости от количества SizeQuantity
    """
    if instance.product:
        total_quantity = instance.product.sizes_and_quantities.aggregate(models.Sum('quantity'))['quantity__sum']
        instance.product.is_active = total_quantity > 0
        instance.product.save()


class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=255, verbose_name="Назва", blank=False, null=False)
    name_en = models.CharField(max_length=255, verbose_name="Назва (англійською)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна", blank=False, null=False)
    price_en = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (англійською)", null=True,
                                   blank=True)
    description = models.TextField(verbose_name="Опис", blank=False, null=False)
    description_en = models.TextField(verbose_name="Опис (англійською)", null=True, blank=True)
    composition = models.TextField(verbose_name="Склад", blank=False, null=False)
    composition_en = models.TextField(verbose_name="Склад (англійською)", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Опубліковано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Додання товару"