from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .serializers import CartSerializer, CartItemSerializer, CartItemPostSerializer
from carts.models import Cart


class CartRetrieveAPIView(RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        return user.carts.all()


class CartItemsViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user).all()

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            return CartItemPostSerializer
        else:
            return CartItemSerializer
