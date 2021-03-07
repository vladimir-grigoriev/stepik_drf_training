from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter


class ItemView(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    ordering_fields = ['id', 'title', 'weight', 'price']
