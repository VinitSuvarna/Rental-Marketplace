from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("items/", include("items.urls")),
    path("rentals/", include("rentals.urls")),
    path("users/", include("users.urls")),
]

# ALWAYS SERVE MEDIA FILES (even when DEBUG=False)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ALWAYS SERVE STATIC FILES
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ---------------------------------------------------------