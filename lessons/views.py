from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions

from .models import Course, Lesson, Enrollment, Progress, Feedback
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CourseSerializer, LessonSerializer, EnrollmentSerializer, ProgressSerializer, FeedbackSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Lesson.objects.all()

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Lesson.objects.filter(course_id=course_id)


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EnrollmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ProgressListCreateView(generics.ListCreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class ProgressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsOwnerOrReadOnly,)
