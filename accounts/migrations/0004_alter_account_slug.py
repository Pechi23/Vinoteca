# Generated by Django 5.0 on 2023-12-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_account_slug_alter_account_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
