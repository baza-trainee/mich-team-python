# Generated by Django 4.2.7 on 2023-12-09 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_created_at_order_status_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
    ]