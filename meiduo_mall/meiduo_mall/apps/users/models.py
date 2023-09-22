# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from meiduo_mall.utils.models import BaseModel
from django.conf import settings
from users import constants

import jwt
import logging


logger = logging.getLogger('django')

class User(AbstractUser):

    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    email_active = models.BooleanField(default=False, verbose_name='邮箱激活状态')
    default_address = models.ForeignKey('Address', on_delete=models.SET_NULL, related_name='users' ,verbose_name='默认地址', null=True, blank=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    
    def generate_email_verify_url(self):
        """生成用户激活邮件"""
        data = {'user_id': self.id, 'email': self.email, 'exp':constants.VERIFY_EMAIL_TOKEN_EXPIRES}
        print(data)
        token = jwt.encode(data, settings.SECRET_KEY).decode()
        verify_url = 'http://www.meiduo.site:8081/success_verify_email.html?token=' + token
        logger.info(f'verify_url是{verify_url}')
        return verify_url
    
    @staticmethod
    def check_verify_email_token(token):
        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        except Exception:
            return None
        else:
            user_id = data.get('user_id')
            email = data.get('email')
            try:
                user = User.objects.get(id=user_id, email=email)
            except User.DoesNotExist:
                return None
            else:
                return user


class Address(BaseModel):
    """用户地址"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    province = models.ForeignKey('areas.Areas', on_delete=models.CASCADE, related_name='province_addresse', verbose_name='省') 
    city = models.ForeignKey('areas.Areas', on_delete=models.CASCADE, related_name='city_addresse', verbose_name='市')
    distinct = models.ForeignKey('areas.Areas', on_delete=models.CASCADE, related_name='distinct_addresse', verbose_name='区')
    place = models.CharField(max_length=20, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    tel = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')


    class Meta:
        db_table = 'tb_address'
        ordering = ['-update_time']