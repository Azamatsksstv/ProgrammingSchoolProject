from django.db import models


class UserTypeChoices(models.TextChoices):
    Teacher = 'Teacher'
    Student = 'Student'
