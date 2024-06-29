from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, is_user=False, is_admin=False, is_recycler=False):
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_user=is_user,
            is_admin=is_admin,
            is_recycler=is_recycler,
            last_login=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_user=True,
            is_admin=True,
            is_recycler=True
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_recycler = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'  # Optionally define the email field

    def __str__(self):
        return self.username        
