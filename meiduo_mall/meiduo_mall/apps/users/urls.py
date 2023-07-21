# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''

from django.urls import path, include
from users.views import UserView


urlpatterns = [
    path('user/', UserView.as_view())
]