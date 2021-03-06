from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


apipatterns = [
    path("items/", include("items.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(apipatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
