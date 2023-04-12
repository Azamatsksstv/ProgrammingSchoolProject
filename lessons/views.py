from rest_framework.decorators import action
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response

from . import services, serializers
from .models import Course, Lesson
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CourseSerializer, LessonSerializer
from users.models import CustomUser


class ListOfCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = IsAdminOrReadOnly,


class ListOfLessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = IsAdminUser,

    def get_queryset(self):
        course_id = self.kwargs['pk']
        queryset = Lesson.objects.filter(course_id=course_id)
        return queryset


class LessonViewSet(viewsets.ViewSet):
    lesson_services: services.LessonServicesInterface = services.LessonServicesV1()

    def create_lesson(self, request, *args, **kwargs):
        serializer = serializers.CreateLessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.lesson_services.create_lesson(data=serializer.validated_data)
        return Response(data)


class CourseViewSet1(viewsets.ViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()

    def create_course(self, request, *args, **kwargs):
        serializer = serializers.CreateCourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.course_services.create_course(data=serializer.validated_data)
        return Response(data)


class MyCoursesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserCoursesSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
