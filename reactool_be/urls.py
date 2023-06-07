from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('projects.urls')),
	path('api/', include('maps.urls')),
	path('api/', include('plans.urls')),
	path('api/', include('panorama.urls')),
	path('api/', include('galleries.urls')),
	path('api/', include('links.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
