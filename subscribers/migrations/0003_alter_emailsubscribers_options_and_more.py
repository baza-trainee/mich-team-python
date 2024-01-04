# Generated by Django 4.2.7 on 2023-12-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_remove_emailsubscribers_subscribed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailsubscribers',
            options={'verbose_name': 'підписника', 'verbose_name_plural': 'Додання підписників'},
        ),
        migrations.AlterField(
            model_name='emailsubscribers',
            name='is_subscribed',
            field=models.BooleanField(default=False, verbose_name='Підписка'),
        ),
    ]