# Generated by Django 2.2.14 on 2022-04-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=1.0),
        ),
    ]
