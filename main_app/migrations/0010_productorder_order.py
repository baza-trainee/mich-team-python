# Generated by Django 4.2.7 on 2024-01-13 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_order_email'),
        ('main_app', '0009_productorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order'),
        ),
    ]
