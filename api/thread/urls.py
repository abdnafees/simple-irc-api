'''
This file contains URL endpoints for Thread app.
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SendMessageView, ThreadCreateView, ThreadListView

urlpatterns = [
    path("", ThreadListView.as_view()),
    path("create-thread/", ThreadCreateView.as_view(), name="create-thread"),
    path("send-message/", SendMessageView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
