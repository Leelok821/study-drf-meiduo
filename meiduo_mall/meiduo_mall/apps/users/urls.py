# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''

from django.urls import path, include
from users.views import UserView, UserNameCountView, UserDetailView, EmailView, VerifyEmailView, AddressViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # 获取token的接口
    path('api/token/', TokenObtainPairView.as_view()),
    # 刷新Token有效期的接口
    path('api/token/refresh/', TokenRefreshView.as_view()),
    # 验证Token的有效性
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('users/', UserView.as_view()),
    path('user/', UserDetailView.as_view()),
    path('usernames/<str:user_name>/count', UserNameCountView.as_view()),

    # 邮箱
    path('email/', EmailView.as_view()), # emails/verification/
    path('emails/verification/', VerifyEmailView.as_view()), 

    # 
    path('addresses/', AddressViewSet.as_view({'get':'list','post':'create'})), 

]


