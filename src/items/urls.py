from django.urls import path
from .views import current_item_view


urlpatterns = [path("<int:pk>", current_item_view, name="current_item")]
