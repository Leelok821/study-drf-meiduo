# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings
 

class FastdfsStorage(Storage):

    def __init__(self, client_conf=None, base_url=None) -> None:
        """
        初始化⽂件存储对象的构造⽅法
        :param client_conf: client.conf的⽂件绝对路径
        :param base_url: 下载⽂件时的域名(ip:端⼝)
        """
        self.client_conf = client_conf or settings.FDFS_CLIENT_CONF
        self.base_url = base_url or settings.FDFS_BASE_URL

    def _open(self):
        """用于打开文件的，但我们自定义存储系统的目的是为了存储到远端的fastdfs服务器上，不需要打开文件"""
        pass

    def _save(self, name, content):
        """
        实现文件存储到fastdfs上
        """
        # 创建客户端
        client = Fdfs_client('meiduo_mall/meiduo_mall/utils/fastdfs/client.conf')

        # 将文件转存fdfs
        res = client.upload_appender_by_buffer(content.read())

        # 判断文件是否上传成功
        if res.get('Status') != 'Upload successed.':
            raise Exception('upload file failed')
        
        file_id = res.get('Remote file_id')
        return file_id


    def exists(self, name: str) -> bool:
        """判断要上传的文件是否已经存在，判断storage中是否已存储了该文件，如果存储了就不会存储，没存储就调用_save()"""
        return False
    
    def url(self, name: str) -> str:
        """返回文件的绝对路径，下载图片时使用"""
        return self.base_url + name