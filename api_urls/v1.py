from django.urls import path, include


urlpatterns = [
    path('', include('lessons.urls.v1')),
]
