# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''


from django.urls import path
from booktest.views import add_hero

urlpatterns = [
    path('/', add_hero),
]