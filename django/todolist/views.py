from django.http.response import Http404
from rest_framework import serializers, status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ToDoList
from .serializer import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

    @action(methods=['create'], detail=False)
    def createToDo(self, request):
        self.serializer_class(data=request.data)
        if self.serializer_class.is_valid():
            self.serializer_class.save()
            return Response(self.serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def getToDo(self, request):
        return Response(data=request.todolist, status=status.HTTP_200_OK)

    @action(methods=['update'], detail=True)
    def updateToDo(self):
        return self.queryset.get(self.request)

    @action(methods=['destroy'], detail=True)
    def deleteToDo(self):
        return self.queryset.get(self.request)
