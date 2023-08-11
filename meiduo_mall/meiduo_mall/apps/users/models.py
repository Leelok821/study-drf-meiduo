from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from users import constants
import jwt
import logging


logger = logging.getLogger('django')

class User(AbstractUser):

    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    email_active = models.BooleanField(verbose_name='邮箱激活状态', default=False)

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


