from django.db import models

# Create your models here.
class EmailSubscribers(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email