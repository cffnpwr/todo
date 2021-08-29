from rest_framework import serializers

from .models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    detail = serializers.CharField()
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = ToDoList
        fields = ('id', 'title', 'detail', 'checked')
