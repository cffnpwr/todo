from django.conf import settings
from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404, request
from rest_framework import generics, permissions, authentication, serializers, status, viewsets, filters
from rest_framework import views
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account, AccountManager
from .serializer import AccountSerializer
import jwt
import time
from todo.settings import SECRET_KEY

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.object.all()
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
    queryset = Account.object.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
        },status=status.HTTP_200_OK)

class AuthLogin(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.object.all()
    serializer_class = AccountSerializer

    def login(self):
        self.user = self.serializer.validated_data['username']

        self.token = jwt_encode_handler(jwt_payload_handler(self.user))

    def get_response(self, request):
        serializer = AccountSerializer(data=request.data)

        response = Response(serializer.data, status=status.HTTP_200_OK)

        return response
    
    def post(self, request):
        self.serializer = AccountSerializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()