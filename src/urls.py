from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('lessons.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
