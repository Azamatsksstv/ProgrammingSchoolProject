from typing import Protocol, OrderedDict
from . import repos, models


class LessonServicesInterface(Protocol):

    def create_lesson(self, data: OrderedDict) -> dict: ...


class LessonServicesV1:
    lesson_repos: repos.LessonReposInterface = repos.LessonReposV1()

    def create_lesson(self, data: OrderedDict) -> dict:
        lesson = self.lesson_repos.create_lesson(data=data)
        print(lesson)

    @staticmethod
    def _create_lesson(title: str) -> None:
        print(f'created lesson {title}')


class CourseServicesInterface(Protocol):
    def create_course(self, data: OrderedDict) -> dict: ...


class CourseServicesV1:
    course_repos: repos.CourseReposInterface = repos.CourseReposV1()

    def create_course(self, data: OrderedDict) -> dict:
        course = self.course_repos.create_course(data=data)
        print(course)
