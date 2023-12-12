# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''
# celery启动文件
from celery import Celery
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mail.setting.dev'


# 创建celery实例
celery_app = Celery('meiduo')
# 加载celery配置
celery_app.config_from_object('celery_tasks.config')
# 自动注册celery任务
celery_app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email', 'celery_tasks.html'])
