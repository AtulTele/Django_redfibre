from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from news.admin import custom_admin_site


urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
