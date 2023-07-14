from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from verifications.constants import SEND_SMS_CODE_INTERVAL,SMS_CODE_REDIS_EXPIRES
from django_redis import get_redis_connection
from rest_framework import status
import random
import logging

logger = logging.getLogger('django')
class SmsCodeVeiw(APIView):

    def get(self, request, mobile):
        """
        1.⽣成短信验证码
        2.保存短信验证码到Redis
        3.集成容联云通讯发送短信验证码
        4.响应结果
        """
        # 判断该手机号规定时间内是否发送过验证码
        redis_con = get_redis_connection('verify_codes')
        if redis_con.get(f'sms_flag_{mobile}'):
            return Response({'message':'频繁发送短信'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 生成验证码
        sms_code = '{0}'.format(random.randint(0,1000000))

        # 创建管道
        

        # 保存短信验证码到Redis
        # 设置缓存内容
        #  key value timeout
        redis_con.set(f'sms_{mobile}', sms_code, SMS_CODE_REDIS_EXPIRES)
        redis_con.set(f'sms_flag_{mobile}', 1, SMS_CODE_REDIS_EXPIRES)
        # 发送短信test
        logger.info(f'send sms_code:{sms_code} to mobile:{mobile}')
        # 响应结果
        return Response({'message':'ok'})
        



