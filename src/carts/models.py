from django.db import models
from items.models import Item
from users.models import User


class Cart(models.Model):
    items = models.ManyToManyField(Item, related_name="carts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=17, decimal_places=2)
