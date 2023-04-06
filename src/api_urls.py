from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('v1/', include('lessons.urls.v1')),
    path('v1/', include('users.urls.v1'))
]
