from rest_framework import serializers
from users.models import User
from rest_framework.response import Response
from django_redis import get_redis_connection
import re


class CreateUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(label='确认密码', write_only=True)
    sms_code = serializers.CharField(label='短信验证码', write_only=True)
    allow = serializers.CharField(label='同意协议', write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username':{
                'min_length':5,
                'max_length':20,
                'error_message':{
                    'min_length': '仅允许5-20个字符的⽤户名',
                    'max_length': '仅允许5-20个字符的⽤户名'
                }
            },
            'password':{
                'write_only':True,
                'min_length':0,
                'max_length':20,
                'error_message':{
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码'
                }
            },
        }

    def validate_mobile(self, data):
        """校验手机号"""
        if not re.match(r'^1[3-9]\d{9}$', data):
            raise serializers.ValidationError('手机号格式错误')
        return data

    def validate_allow(self, data):
        """校验协议"""
        if data != True:
            raise serializers.ValidationError('请同意用户协议')
        return data
    
    def validate(self, attrs):
        # 判断两次密码
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码输入不一致')
        
        # 判断短信验证码
        redis_con = get_redis_connection('verify_codes')
        sms_code = redis_con.get(f'sms_{attrs["mobile"]}')
        if sms_code != attrs['sms_code']:
            raise serializers.ValidationError('验证码不一致')

        