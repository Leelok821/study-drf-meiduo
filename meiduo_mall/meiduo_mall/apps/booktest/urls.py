# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''


from django.urls import path
from booktest.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('books/', BookModelViewSet.as_view({'get':'list','post':'create'})),
    path('books/<int:id>/', BookModelViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    # path()
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新Token有效期的接口
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证Token的有效性
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

router = DefaultRouter()
router.register('books',BookModelViewSet)
router.register('heros',HeroModelViewSet)
urlpatterns += router.urls