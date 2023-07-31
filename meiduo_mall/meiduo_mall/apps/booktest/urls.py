# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''


from django.urls import path
from booktest.views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns = [
    # path('books/', BookModelViewSet.as_view({'get':'list','post':'create'})),
    # path('books/<int:id>/', BookModelViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]

router = DefaultRouter()
router.register('books',BookModelViewSet)
urlpatterns += router.urls