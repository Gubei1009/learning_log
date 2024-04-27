"""Defines url patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^parse/$', views.parse, name='parse'),
    # 米贝分享 免费节点www.mibei77.com
    url(r'^getFreeSS/$', views.getFreeSS, name='getFreeSS'),

]
