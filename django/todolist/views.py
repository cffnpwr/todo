from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .models import ToDoList
from .serializer import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.username

        toDoSerializer = self.get_serializer(data=data)
        if toDoSerializer.is_valid():
            toDoSerializer.save()
            return Response(toDoSerializer.data, status=status.HTTP_201_CREATED)
        return Response(toDoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        return Response(data=request.todolist, status=status.HTTP_200_OK)
