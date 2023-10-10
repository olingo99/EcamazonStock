from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Quantity = models.IntegerField(default=0)
    Location = models.CharField(max_length=200)
    ProductName = models.CharField(max_length=200)

class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    OrderDate = models.DateTimeField(auto_now_add=True)
    UserId = models.IntegerField(db_index=True)
    State = models.TextField(choices=[("Sent","Sent"),("Delivered","Delivered"),("Processing","Processing")])
    ParcelId = models.IntegerField()


class OrderProductLink(models.Model):
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete = models.CASCADE)
    ProductQuantity = models.IntegerField()



