# -*- coding:utf-8 -*-
# Author : Dexter
# Data : 2018/8/12  上午11:13


from django.urls import path
from . import views


urlpatterns = [

    path('', views.msgproc),
]
