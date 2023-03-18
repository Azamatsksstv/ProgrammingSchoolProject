from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some/', include('djoser.urls')),
    re_path(r'users/', include('djoser.urls.authtoken')),
    path('drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include('lessons.urls')),
]
