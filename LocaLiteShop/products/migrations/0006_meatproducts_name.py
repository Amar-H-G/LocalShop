# Generated by Django 5.1.3 on 2024-11-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_meatproducts_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='meatproducts',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
