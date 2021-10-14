from django.db import transaction
from django.http.response import Http404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Account
from .serializer import AccountSerializer


class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(methods=['get'], detail=True)
    def getUserInfo(self, request):
        return Response(data={
            'username': request.user.username,
        }, status=status.HTTP_200_OK)

    @action(methods=['update'], detail=True)
    def updateUserInfo(self):
        self.lookup_field = 'username'

        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except Account.DoesNotExist:
            return Http404

    @action(methods=['destroy'], detail=True)
    def deleteUser(self):
        self.lookup_field = 'username'

        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except Account.DoesNotExist:
            return Http404
