from rest_framework import serializers
from .models import Cart, CartItem
from items.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "item", "item_id", "quantity", "price", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ["id", "items", "total_cost"]


class CartItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "item", "quantity", "price", "total_price"]
        read_only_fields = ["id", "price", "total_price"]
