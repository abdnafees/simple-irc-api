from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ServerList, CreateServer


urlpatterns = [
    path("", ServerList.as_view()),
    path("create-server/", CreateServer.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
