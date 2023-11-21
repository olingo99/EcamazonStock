from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["ProductCode", "Quantity", "ProductName", "WhareHouseId", "CategoryId"]



class OrderProductLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductLink
        fields = ["OrderId","ProductId","HandlerId","ProductQuantity"]

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductLinkSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["OrderId","OrderDate","UserId","State", "ParcelId", "Products"]


class WhareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhareHouse
        fields = ["WhareHouseId","WhareHouseName","WhareHouseLocation"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["CategoryId","CategoryName","CategoryDescription"]

class HandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handler
        fields = ["HandlerId","HandlerName","HandlerSurname","HandlerAddress"]