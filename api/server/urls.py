'''
This file contains URL endpoints for Server app.
'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server.views import CreateServer, ServerList

urlpatterns = [
    path("", ServerList.as_view()),
    path("create-server/", CreateServer.as_view(), name="create-server"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
