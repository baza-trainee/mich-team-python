from django.db import models


class EmailSubscribers(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=False, verbose_name="Підписка")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "підписника"
        verbose_name_plural = "Додання підписників"