# Generated by Django 4.2.4 on 2024-03-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0018_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="Landmark",
            field=models.TextField(),
        ),
    ]
