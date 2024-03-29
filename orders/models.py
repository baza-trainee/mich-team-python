from django.conf import settings
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name="Користувач")
    email = models.EmailField(max_length=40, verbose_name="Пошта")
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    delivery_method = models.CharField(max_length=50, verbose_name="Метод доставки")
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name="Країна")
    street = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вулиця")
    city = models.CharField(max_length=50, verbose_name="Місто")
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name="Область")
    zip_code = models.CharField(max_length=10, null=True, blank=True, verbose_name="Поштовий індекс")
    department = models.CharField(max_length=100, null=True, blank=True, verbose_name="Відділення")
    house_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер будинку")
    apartment_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер квартири")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    STATUS_CHOICES = [
        ('Новий', 'Новий'),
        ('Прийнято', 'Прийнято'),
        ('Скасовано', 'Скасовано'),
        ('Оплачено', 'Оплачено'),
        ('В дорозі', 'В дорозі'),
        ('Виконано', 'Виконано'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новий', verbose_name="Статус")

    def __str__(self):
        return str(self.created_at)


    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"