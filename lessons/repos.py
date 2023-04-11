from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from . import models


class LessonReposInterface(Protocol):
    def create_lesson(self, data: OrderedDict) -> models.Lesson: ...

    def get_lesson(self, data: OrderedDict): ...


class LessonReposV1:
    model = models.Lesson

    def create_lesson(self, data: OrderedDict) -> models.Lesson:
        return self.model.objects.create_lesson(**data)

    def get_lesson(self, data: OrderedDict):
        lesson = get_object_or_404(self.model, id=data["id"])
        return lesson
