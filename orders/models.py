from django.conf import settings
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from main_app.models import Product, SizeQuantity


class Order(models.Model):
    carts = models.ManyToManyField(Cart, blank=True, verbose_name="Корзіни")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name="Користувач")
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    delivery_method = models.CharField(max_length=50, verbose_name="Метод доставки")
    country = models.CharField(max_length=50, verbose_name="Країна")
    street = models.CharField(max_length=100, verbose_name="Вулиця")
    city = models.CharField(max_length=50, verbose_name="Місто")
    state = models.CharField(max_length=50, verbose_name="Область")
    zip_code = models.CharField(max_length=10, verbose_name="Поштовий індекс")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    STATUS_CHOICES = [
        ('Прийнято', 'Прийнято'),
        ('Скасовано', 'Скасовано'),
        ('Оплачено', 'Оплачено'),
        ('В дорозі', 'В дорозі'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Прийнято', verbose_name="Статус")

    def __str__(self):
        return str(self.created_at)


    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"