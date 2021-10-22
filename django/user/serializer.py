from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Account

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

    def update(delf, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()

        return instance
