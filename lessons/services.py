from typing import Protocol, OrderedDict
from . import repos, models


class LessonServicesInterface(Protocol):

    def create_lesson(self, data: OrderedDict) -> dict:...


class LessonServicesV1:
    lesson_repos: repos.LessonReposInterface = repos.LessonReposV1()

    def create_lesson(self, data: OrderedDict) -> dict:
        lesson = self.lesson_repos.create_lesson(data=data)
        self._create_lesson(title=lesson.title)
        return {
            'lesson': lesson,
        }

    @staticmethod
    def _create_lesson(title: str) -> None:
        print(f'created lesson {title}')

