from django.db import models
from django.contrib.auth.models import User





class WhareHouse(models.Model):
    WhareHouseId = models.AutoField(primary_key=True)
    WhareHouseName = models.CharField(max_length=200)
    WhareHouseLocation = models.CharField(max_length=200)


class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=200)
    CategoryDescription = models.CharField(max_length=200)

class Product(models.Model):
    ProductCode = models.AutoField(primary_key=True)
    Quantity = models.IntegerField(default=0)
    # ProductCode = models.CharField(primary_key=True, max_length=)
    # Location = models.CharField(max_length=200)
    ProductName = models.CharField(max_length=200)
    WhareHouseId = models.ForeignKey(WhareHouse, on_delete=models.CASCADE)
    CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    OrderDate = models.DateTimeField(auto_now_add=True)
    UserId = models.IntegerField(db_index=True)
    State = models.TextField(choices=[("Sent","Sent"),("Delivered","Delivered"),("Processing","Processing")])
    ParcelId = models.IntegerField()
    Products = models.ManyToManyField(Product, through='OrderProductLink')

class Handler(models.Model):
    HandlerId = models.AutoField(primary_key=True)
    HandlerName = models.CharField(max_length=200)
    HandlerSurname = models.CharField(max_length=200)
    HandlerAddress = models.CharField(max_length=200)

class OrderProductLink(models.Model):
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete = models.CASCADE)
    HandlerId = models.ForeignKey(Handler, on_delete = models.CASCADE)
    ProductQuantity = models.IntegerField()



