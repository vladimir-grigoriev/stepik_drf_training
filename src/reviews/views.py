from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Review


@api_view(http_method_names=["GET"])
def all_reviews_view(request):
    result = Review.objects.all()
    to_response = []

    for r in result:
        to_response.append({"id": r.id, "author": r.author.username, "text": r.text})

    return Response(to_response)
