from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from items.views import ItemView
from users.views import UserCreateAPIView, UserRetrieveUpdateAPIView
from carts.views import CartRetrieveAPIView, CartItemsViewSet


schema_view = get_schema_view(
    openapi.Info(title="Stepic DRF API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register("items", ItemView, basename="items")
router.register("carts/items", CartItemsViewSet, basename="cart_items")

apipatterns = [
    path("users/auth/register", UserCreateAPIView.as_view()),
    path("users/auth/login", views.obtain_auth_token),
    path("users/current", UserRetrieveUpdateAPIView.as_view()),
    path("carts/", CartRetrieveAPIView.as_view()),
    path("", include(router.urls)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(apipatterns)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
