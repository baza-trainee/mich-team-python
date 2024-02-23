from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from subscribers.models import EmailSubscribers
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)

    def create_user(self, email, password=None, is_subscribed=False, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=email.lower(), is_subscribed=is_subscribed, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if is_subscribed:
            EmailSubscribers.objects.create(email=email.lower(), is_subscribed=True)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, default=False)
    first_name = models.CharField(max_length=30, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, verbose_name="Призвище")
    is_active = models.BooleanField(default=True, verbose_name="Активний")
    is_staff = models.BooleanField(default=False, verbose_name="Адмін")
    is_subscribed = models.BooleanField(verbose_name="Підписан")
    phone = models.CharField(max_length=15, verbose_name="Телефон", null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'is_subscribed']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "користувача"
        verbose_name_plural = "Користувачі"


class UserAddresses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='addresses',
                             null=True, blank=True, verbose_name="Користувач")
    delivery_method = models.CharField(max_length=50, null=True, blank=True, verbose_name="Метод доставки")
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name="Країна")
    street = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вулиця")
    city = models.CharField(max_length=50, verbose_name="Місто")
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name="Область")
    zip_code = models.CharField(max_length=10, null=True, blank=True, verbose_name="Поштовий індекс")
    department = models.CharField(max_length=100, null=True, blank=True, verbose_name="Відділення")
    house_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер будинку")
    apartment_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер квартири")

    def __str__(self):
        return f"{self.user} - {self.city}, {self.street}"
    class Meta:
        verbose_name = "адреса"
        verbose_name_plural = "Адреси"