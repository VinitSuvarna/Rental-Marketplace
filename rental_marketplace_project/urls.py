from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),      # or whatever your main app is
    path("items/", include("items.urls")),
    path("rentals/", include("rentals.urls")),
    path("users/", include("users.urls")),
]

# 👇 ADD THIS at the end (outside the list)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
