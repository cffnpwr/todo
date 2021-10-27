from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from collections import OrderedDict

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
        queryset = self.filter_queryset(self.get_queryset())
        toDoSerializer = self.get_serializer(queryset, many=True)

        outputData = []
        for data in toDoSerializer.data :
            if data['user'] == request.user.username :
                outputData.append(data)

        return Response(outputData, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if serializer.data['user'] == request.user.username :    
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.get_serializer(instance).data['user'] == request.user.username :
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if self.get_serializer(instance).data['user'] == request.user.username :
            toDoSerializer = self.get_serializer(instance, data=request.data)
            toDoSerializer.is_valid(raise_exception=True)
            self.perform_update(toDoSerializer)

            return Response(toDoSerializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
