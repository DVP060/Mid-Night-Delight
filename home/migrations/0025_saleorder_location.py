# Generated by Django 4.2.4 on 2024-03-04 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0024_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="saleorder",
            name="location",
            field=models.URLField(null=True),
        ),
    ]
