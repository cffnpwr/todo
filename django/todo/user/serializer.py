from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import RequestDataTooBig
from django.db import models
from django.db.models import fields
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Account, AccountManager

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return Account.object.create_user(request_data=validated_data)
