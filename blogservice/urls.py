from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.api.routers import router as posts_api_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(posts_api_router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
