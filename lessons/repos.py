from typing import Protocol, OrderedDict

from django.http import JsonResponse
from rest_framework.generics import get_object_or_404

from . import models


class LessonReposInterface(Protocol):
    def create_lesson(self, data: OrderedDict) -> models.Lesson: ...

    def get_lesson(self, data: OrderedDict): ...


class LessonReposV1:
    model = models.Lesson

    def create_lesson(self, data: OrderedDict) -> dict:
        lesson = self.model.objects.create(**data)
        return {
            'lesson': lesson,
        }

    def get_lesson(self, data: OrderedDict):
        lesson = get_object_or_404(self.model, id=data["id"])
        return lesson


class CourseReposInterface(Protocol):
    def create_course(self, data: OrderedDict) -> models.Course: ...

    def get_course(self, data: OrderedDict): ...


class CourseReposV1:
    model = models.Course

    def create_course(self, data: OrderedDict) -> dict:
        course = self.model.objects.create(**data)
        return {
            'course': course,
        }

    def get_course(self, data: OrderedDict):
        course = get_object_or_404(self.model, id=data["id"])
        return course
