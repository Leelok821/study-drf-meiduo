 
import logging

from celery_tasks.main import celery_app

logger = logging.getLogger('django')

@celery_app.task(name='send_sms_code')
def send_sms_code(mobile, sms_code):
    """发送短信验证码"""
    logger.info(f'celery send sms_code:{sms_code} to mobile:{mobile}')
