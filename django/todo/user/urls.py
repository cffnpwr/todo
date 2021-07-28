from django.conf.urls import include, url
from rest_framework import routers
from .views import AuthLogin, AuthRegister, AuthInfoGetView

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^mypage/$', AuthInfoGetView.as_view()),
    url(r'^login/$', AuthLogin.as_view()),
]