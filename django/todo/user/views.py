from django.db import transaction
from django.http.response import Http404
from rest_framework import generics, permissions, status
from rest_framework_jwt.settings import api_settings
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


class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
        }, status=status.HTTP_200_OK)


class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except Account.DoesNotExist:
            return Http404


class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except Account.DoesNotExist:
            return Http404
