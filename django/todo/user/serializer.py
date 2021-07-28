from django.contrib.auth import update_session_auth_hash
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Account, AccountManager

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return Account.object.create_user(request_data=validated_data)