# Generated by Django 5.0 on 2024-01-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_remove_account_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
