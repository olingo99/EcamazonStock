# Generated by Django 4.2.5 on 2023-10-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.IntegerField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('UserId', models.IntegerField(db_index=True)),
                ('State', models.TextField(choices=[('Sent', 'Sent'), ('Delivered', 'Delivered'), ('Processing', 'Processing')])),
                ('ParcelId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductId', models.IntegerField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField(default=0)),
                ('Location', models.CharField(max_length=200)),
                ('ProductName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductQuantity', models.IntegerField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StockAPI.order')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StockAPI.product')),
            ],
        ),
    ]
