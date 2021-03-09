from django.db import models
from items.models import Item
from users.models import User


class Cart(models.Model):
    items = models.ManyToManyField(Item, related_name="carts", through="CartItem")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")

    @property
    def total_cost(self):
        result = sum(i.total_price for i in self.items.all())
        return result


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=17, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.price
