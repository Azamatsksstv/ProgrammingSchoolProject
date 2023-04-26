from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token

from lessons.models import Course
from . import serializers, services, models


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.user_services.create_user(data=serializer.validated_data)

        return Response(data)

    def verify_user(self, request, *args, **kwargs):
        serializer = serializers.VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.user_services.verify_user(data=serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create_token(self, request, *args, **kwargs):
        serializer = serializers.CreateTokenSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        tokens = self.user_services.create_token(data=serializer.validated_data)

        return Response(tokens)

    def verify_token(self, request, *args, **kwargs):
        serializer = serializers.VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = self.user_services.verify_token(data=serializer.validated_data)

        return Response(tokens)


class UserCapabilityViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()
    # permission_classes = permissions.IsAdminUser

    def join_course(self, request, *args, **kwargs):
        user = request.user
        print(user)
        user.courses.add(Course.objects.get(id=1))
        return Response({'user_email': user.email})
