from django.urls import path
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListUsers, LoginView, RegisterUser


urlpatterns = [
    path("", ListUsers.as_view()),
    path("login/", views.obtain_auth_token),
    path("create-user/", RegisterUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
