# Generated by Django 4.2.5 on 2023-11-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0003_category_handler_wharehouse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ParcelId',
            field=models.CharField(max_length=10),
        ),
    ]
