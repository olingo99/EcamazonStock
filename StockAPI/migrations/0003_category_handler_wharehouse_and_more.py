# Generated by Django 4.2.5 on 2023-11-21 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0002_alter_order_orderid_alter_product_productid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=200)),
                ('CategoryDescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('HandlerId', models.AutoField(primary_key=True, serialize=False)),
                ('HandlerName', models.CharField(max_length=200)),
                ('HandlerSurname', models.CharField(max_length=200)),
                ('HandlerAddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WhareHouse',
            fields=[
                ('WhareHouseId', models.AutoField(primary_key=True, serialize=False)),
                ('WhareHouseName', models.CharField(max_length=200)),
                ('WhareHouseLocation', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ProductId',
            new_name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Location',
        ),
        migrations.AddField(
            model_name='order',
            name='Products',
            field=models.ManyToManyField(through='StockAPI.OrderProductLink', to='StockAPI.product'),
        ),
        migrations.AddField(
            model_name='orderproductlink',
            name='HandlerId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StockAPI.handler'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='CategoryId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StockAPI.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='WhareHouseId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StockAPI.wharehouse'),
            preserve_default=False,
        ),
    ]
