from rest_framework import serializers
from .models import Course, Lesson, Enrollment, Progress, Feedback


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'enrollment_date', 'progress', 'course_title']
        read_only_fields = ['user', 'enrollment_date']


class ProgressSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)

    class Meta:
        model = Progress
        fields = ['user', 'lesson', 'completion_status', 'score', 'user_username', 'lesson_title']
        read_only_fields = ['user', 'lesson']


class FeedbackSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    course_title = serializers.CharField(source='lesson.course.title', read_only=True)

    class Meta:
        model = Feedback
        fields = ['user', 'lesson', 'rating', 'comments', 'user_username', 'lesson_title', 'course_title']
        read_only_fields = ['user']
