# Generated by Django 4.2.4 on 2024-03-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0022_alter_address_landmark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saleorder",
            name="Payment_Type",
            field=models.CharField(max_length=30),
        ),
    ]
