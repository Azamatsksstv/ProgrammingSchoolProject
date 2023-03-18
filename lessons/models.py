from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz_questions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    progress = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'course')


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completion_status = models.BooleanField(default=False)
    score = models.FloatField(default=0)

    class Meta:
        unique_together = ('user', 'lesson')


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    # course = lesson.
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.lesson:
            return f'{self.lesson.title} feedback by {self.user.username}'
        elif self.course:
            return f'{self.course.title} feedback by {self.user.username}'
        else:
            return 'Invalid feedback'

