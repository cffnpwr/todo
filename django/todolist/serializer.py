from rest_framework import serializers

from .models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    detail = serializers.CharField()
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'title', 'detail', 'checked')
