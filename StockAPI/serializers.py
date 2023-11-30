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

# class ProductOrderLinkSerializer(serializers.ModelSerializer):
#     ProductId = ProductSerializer(read_only=True)

#     class Meta:
#         model = OrderProductLink
#         fields = ["OrderId", "ProductId", "HandlerId", "ProductQuantity"]
class ProductOrderLinkSerializer(serializers.ModelSerializer):
    ProductCode = serializers.ReadOnlyField(source='ProductId.ProductCode')
    Quantity = serializers.ReadOnlyField(source='ProductQuantity')

    class Meta:
        model = OrderProductLink
        fields = ["ProductCode", "Quantity"]

# class OrderSerializer(serializers.ModelSerializer):
#     Products = OrderProductLinkSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ["OrderId","OrderDate","UserId","State", "ParcelId", "Products"]

# class OrderSerializer(serializers.ModelSerializer):
#     Products = ProductOrderLinkSerializer(source='orderproductlink_set', many=True, read_only=True)

#     class Meta:
#         model = Order
#         fields = ["OrderId", "OrderDate", "UserId", "State", "ParcelId", "Products"]
class OrderSerializer(serializers.ModelSerializer):
    Products = ProductOrderLinkSerializer(source='orderproductlink_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["OrderId", "UserId", "ParcelId", "Products"]

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