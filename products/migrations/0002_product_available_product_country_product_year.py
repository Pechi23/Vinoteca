# Generated by Django 5.0 on 2024-01-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="year",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]