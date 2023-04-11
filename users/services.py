from typing import Protocol, OrderedDict

from rest_framework_simplejwt import tokens
from django.core.cache import cache
from rest_framework.exceptions import ValidationError

from . import repos, models


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None:...

    def create_token(self, data: OrderedDict) -> dict:...

    def verify_user(self, data: OrderedDict) -> models.CustomUser | None: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repos.create_user(data=data)
        self._send_letter_to_email(email=user.email)

    @staticmethod
    def _send_letter_to_email(email: str) -> None:
        print(f'send letter to {email}')

    def create_token(self, data: OrderedDict) -> tokens.AccessToken:
        user = self.user_repos.get_user(data=data)

        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    def verify_user(self, data: OrderedDict) -> models.CustomUser | None:
        user_data = cache.get(data['session_id'])

        if not user_data:
            raise ValidationError

        if data['code'] != user_data['code']:
            raise ValidationError

        user = self.user_repos.create_user(data={
            'email': user_data['email'],
        })
        self._send_letter_to_email(user=user)
