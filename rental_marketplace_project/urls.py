# rental_marketplace_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 👈 IMPORT SETTINGS
from django.conf.urls.static import static # 👈 IMPORT STATIC FUNCTION

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # 'name="index"' is likely here
    path('items/', include('items.urls')),
    path('users/', include('users.urls')),
]

# 👇 ADD THIS BLOCK AT THE END OF THE FILE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)