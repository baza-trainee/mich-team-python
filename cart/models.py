from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from main_app.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        if self.user:
            return f"{self.user}"
        elif self.session_id:
            return f"Cart with Session ID: {self.session_id}"
        else:
            return "Unknown Cart"
