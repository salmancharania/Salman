from django.conf.urls import *
from django.conf.urls import url
from django.contrib import admin
from .import views


urlpatterns = [
      url(r'^$', views.IndexView.as_view(), name='index'),
      ]
