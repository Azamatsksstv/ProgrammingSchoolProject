from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from . import serializers, services


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.user_services.create_user(data=serializer.validated_data)

        return Response(data)
