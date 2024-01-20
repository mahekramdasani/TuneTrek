# music/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),  # Include the URLs from the 'api' app
    path('', include('musicrecommend.urls')),  # Include the URLs from the 'musicrecommend' app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])