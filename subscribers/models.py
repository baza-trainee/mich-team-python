from django.db import models


class EmailSubscribers(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email