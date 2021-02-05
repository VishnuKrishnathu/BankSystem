# Generated by Django 3.0.5 on 2021-02-05 05:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='account_balance',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7000)]),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]