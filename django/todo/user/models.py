from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, _user_has_perm

from django.utils.translation import ugettext_lazy as _

class AccountManager(BaseUserManager):
    def create_user(self, request_data):
        user = self.model(username=request_data['username'])
        user.set_password(request_data['password'])
        user.save()
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True)   
    object = AccountManager()

    USERNAME_FIELD = 'username'

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'
