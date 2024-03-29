# Generated by Django 4.2.7 on 2024-02-22 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method', models.CharField(max_length=50, verbose_name='Метод доставки')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Країна')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вулиця')),
                ('city', models.CharField(max_length=50, verbose_name='Місто')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='Область')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Поштовий індекс')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='Відділення')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер будинку')),
                ('appartment_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер квартири')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'адреса',
                'verbose_name_plural': 'Адреси',
            },
        ),
    ]
