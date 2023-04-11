from rest_framework import serializers

from users.models import CustomUser
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserCoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'courses',)
