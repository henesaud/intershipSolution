# Generated by Django 2.2.14 on 2022-04-26 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220426_0046'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='stripe_charge_id',
        ),
        migrations.DeleteModel(
            name='Refund',
        ),
    ]
