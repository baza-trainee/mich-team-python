# Generated by Django 4.2.7 on 2024-01-11 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='sizequantity',
            options={'verbose_name': 'Розмір', 'verbose_name_plural': 'Розміри'},
        ),
    ]
