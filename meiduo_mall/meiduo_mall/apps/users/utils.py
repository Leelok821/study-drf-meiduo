# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''

import re
from typing import Any, Optional

from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

from users.models import User

from django.contrib.auth.backends import ModelBackend



def get_user_by_account(account):
    """根据传入的账号获取用户信息"""
    try:
        if re.match('^1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
            
    except User.DoesNotExist:
        return None
    else:
        return user


class MyModelBackend(ModelBackend):
    """修改用户认证系统的后段，支持多账号登陆"""

    def authenticate(self, request: HttpRequest, username: str, password: str, **kwargs: Any):
        user = get_user_by_account(username)
        if user.check_password(password) and self.user_can_authenticate(user):
            return user

    