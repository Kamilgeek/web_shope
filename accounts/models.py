from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Core
# Create your models here.
class Account(AbstractUser, Core):
    """
    Класс юзеров наследуется от 2 суперклассов
    """
    pass