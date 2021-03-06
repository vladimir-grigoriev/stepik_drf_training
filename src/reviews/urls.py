from django.urls import path
from .views import all_reviews_view


urlpatterns = [path("", all_reviews_view)]
