from django.urls import path
from rest_framework.routers import DefaultRouter
from lessons.views import *
from lessons.models import Course

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('my_courses/', MyCoursesViewSet.as_view({'get': 'list'})),
    path('courses/<int:pk>/join/', JoinCourseViewSet.as_view({'post': 'join'}), name='course-join'),
    path('create_lesson/', LessonViewSet1.as_view({'post': 'create_lesson'})),
    path('create_course/', CourseViewSet1.as_view({'post': 'create_course'})),
    # path('courses/<int:pk>/join/', )
    # path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    # path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),
    # path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    # path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
]


urlpatterns += router.urls
