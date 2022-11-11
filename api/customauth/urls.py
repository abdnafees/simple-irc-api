'''
This file contains URL endpoints for Customauth app.
'''
from django.urls import path
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

from customauth.views import ListUsers, RegisterUser

urlpatterns = [
    path('', ListUsers.as_view()),
    path('login/', views.obtain_auth_token, name='login'),
    path('create-user/', RegisterUser.as_view(), name='create-user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
