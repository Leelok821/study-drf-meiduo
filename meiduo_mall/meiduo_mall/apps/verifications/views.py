from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from django_redis import get_redis_connection

import random

class SmsCodeVeiw(APIView):

    def get(self, request, mobile):
        """
        1.
        2.⽣成短信验证码
        3.保存短信验证码到Redis
        4.集成容联云通讯发送短信验证码
        5.响应结果
        """
        # ⽣成短信验证码
        sms_code = '%06d' % random.randint(0,999999)
        
        # 存储短信验证码内容到redis数据库
        redis_conn = get_redis_connection('verify_codes')
        # redis_conn.setex("sms_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 发送短信验证码
        # CCP().send_template_sms(mobile,[sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], 1) 
        # 响应发送短信验证码结果
        return Response({"message": "OK"})



