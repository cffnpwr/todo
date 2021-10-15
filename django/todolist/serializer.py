from rest_framework import serializers

from .models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    detail = serializers.CharField()
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = ToDoList
        fields = ('user', 'title', 'detail', 'checked')
