from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)


class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        user = self.model(username=request_data['username'])
        user.set_password(request_data['password'])
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        requestData = {
            'username': username,
            'password': password
        }

        user = self.create_user(requestData)
        user.is_admin = True
        user.is_staff = True
        user.save()

        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'
