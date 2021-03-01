from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Item


@api_view(http_method_names=['GET'])
def current_item_view(request, pk):
    result = get_object_or_404(Item, pk=pk)

    if result:
        return Response({
            'id': result.id,
            'title': result.id,
            'description': result.description,
            'image': result.image.url,
            'weight': result.weight,
            'price': result.price
        })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

