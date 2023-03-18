from django.urls import path
from .views import (
    CourseListCreateView, CourseRetrieveUpdateDestroyView,
    LessonListCreateView, LessonRetrieveUpdateDestroyView,
    EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView,
    ProgressListCreateView, ProgressRetrieveUpdateDestroyView,
    FeedbackListCreateView, FeedbackRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-retrieve-update-destroy'),
    path('progresses/', ProgressListCreateView.as_view(), name='progress-list-create'),
    path('progresses/<int:pk>/', ProgressRetrieveUpdateDestroyView.as_view(), name='progress-retrieve-update-destroy'),
    path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedbacks/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-retrieve-update-destroy'),
]
