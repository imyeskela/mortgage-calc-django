from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from main.models import Mortgage


class User(AbstractUser):
    mortgage = models.ManyToManyField(Mortgage)
    email = models.EmailField('Email', unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
