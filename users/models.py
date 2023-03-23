from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name=_('Email'))

