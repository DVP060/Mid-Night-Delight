# Generated by Django 5.0.2 on 2024-03-04 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_customer_img_customer_cus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('totalprice', models.IntegerField(null=True)),
                ('product_status', models.IntegerField(null=True)),
                ('orderid', models.IntegerField(null=True)),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
                ('food_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.food_item')),
            ],
        ),
    ]
