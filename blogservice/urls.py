from django.contrib import admin
from django.urls import path, include
from posts.api.routers import router as posts_api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(posts_api_router.urls))
]
