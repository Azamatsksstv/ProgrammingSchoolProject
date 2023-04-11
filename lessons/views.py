from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response

from . import services, serializers
from .models import Course, Lesson
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CourseSerializer, LessonSerializer
from users.models import CustomUser


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MyCoursesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserCoursesSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)


class LessonViewSet(viewsets.ViewSet):
    lesson_services: services.LessonServicesInterface = services.LessonServicesV1()

    def create_lesson(self, request, *args, **kwargs):
        serializer = serializers.CreateLessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.lesson_services.create_lesson(data=serializer.validated_data)

        return Response(data)


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


