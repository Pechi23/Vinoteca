# Generated by Django 5.0 on 2024-01-02 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_cart_user_delete_account"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CartProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(to="accounts.cartproduct"),
        ),
    ]