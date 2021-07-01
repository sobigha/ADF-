"""Urls python file"""
from django.urls import path
#pylint: disable=E0402
from .views import index, user

urlpatterns = [
  #  path('news/', News, name='News'),
    path('register/', index, name='index'),
    path('user/', user, name='user')
]
