from django.conf import settings
from django.db import models
from main_app.models import Product
from orders.models import Order


# from orders.models import Order


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=2,
                            choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'),
                                     ('XL', 'Extra Large')], null=True, blank=True, verbose_name="Size")
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - Розмір: {self.size} - К-сть: {self.quantity}"



    # class Meta:
    #     indexes = [models.Index(fields=['session_id', 'user', 'is_active'])] #TODO: read about it (postgre specifice)
