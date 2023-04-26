from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from lessons.models import Course
from . import models


class UserReposInterface(Protocol):

    def create_user(self, data: OrderedDict) -> models.CustomUser: ...

    def get_user(self, data: OrderedDict): ...

    def join_course(self, user_id: str, course_id: str):...


class UserReposV1:
    model = models.CustomUser

    def create_user(self, data: OrderedDict) -> models.CustomUser:
        return self.model.objects.create_user(**data)

    def get_user(self, data: OrderedDict):
        user = get_object_or_404(self.model, email=data["email"])
        if not user.check_password(data['password']):
            raise self.model.DoesNotExist
        return user

    def join_course(self, user_id: str, course_id: str):
        user = self.model.objects.get(id=user_id)
        course = Course.objects.get(id=course_id)
        user.courses.add(course)
