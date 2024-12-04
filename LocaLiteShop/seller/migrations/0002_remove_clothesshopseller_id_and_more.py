# Generated by Django 5.1.3 on 2024-11-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothesshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='drinksshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='electronicsshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='foodsshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='fruitsshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='groceryshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='housecomponentshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='icecreamshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meatshopseller',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vegetablesshopseller',
            name='id',
        ),
        migrations.AddField(
            model_name='clothesshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='drinksshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='electronicsshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='foodsshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='fruitsshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='groceryshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='housecomponentshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='icecreamshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='meatshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='vegetablesshopseller',
            name='seller_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
