from django.conf.urls import url
from .views import AuthInfoDeleteView, AuthInfoUpdateView, AuthRegister, AuthInfoGetView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^mypage/$', AuthInfoGetView.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^auth_update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view())
]
