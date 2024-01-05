# Generated by Django 5.0 on 2024-01-03 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0011_cartproduct_alter_cart_products"),
        ("products", "0002_product_available_product_country_product_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_products",
                to="products.product",
            ),
        ),
    ]