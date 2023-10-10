from rest_framework import serializers
from .models import Product, Order, OrderProductLink

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["ProductId", "Quantity", "Location", "ProductName"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["OrderId","OrderDate","UserId","State", "ParcelId"]


class OrderProductLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductLink
        fields = ["OrderId","ProductId","ProductQuantity"]