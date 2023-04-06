from django.urls import path
from rest_framework.routers import DefaultRouter
from lessons.views import *
from lessons.models import Course

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
# router.register(r'courses/<int:pk>/', CourseViewSet)


urlpatterns = [
    # path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    # path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),
    # path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    # path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    # path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    # path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-retrieve-update-destroy'),
    # path('progresses/', ProgressListCreateView.as_view(), name='progress-list-create'),
    # path('progresses/<int:pk>/', ProgressRetrieveUpdateDestroyView.as_view(), name='progress-retrieve-update-destroy'),
    # path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    # path('feedbacks/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-retrieve-update-destroy'),
    # path('courses/<int:course_id>/lessons/', LessonListAPIView.as_view(), name='course-lessons-list'),
]


urlpatterns += router.urls
