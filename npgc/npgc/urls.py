from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('pycoder/npgc/admin/', admin.site.urls),
    path('', include('user.urls')),  # Redirect the root URL to the login page
    # path('npgc/', include('user.urls')),  # Include URLs for user app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
