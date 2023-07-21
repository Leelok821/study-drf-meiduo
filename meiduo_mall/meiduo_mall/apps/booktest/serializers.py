# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''
from rest_framework import serializers

class BookInfoSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True,label='书籍编号')
    btitle = serializers.CharField(max_length=20,min_length=3,label='名称')
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(default=0,min_value=0,label='阅读量')
    bcomment = serializers.IntegerField(default=0,max_value=50,label='评论量')
    is_delete = serializers.BooleanField(default=False,label='逻辑删除')

class HeroInfoSerializer(serializers.Serializer):
    GENDER = ((0, 'male'), (1, 'female'))
    id = serializers.IntegerField(label='ID',read_only=True)
    hname = serializers.CharField(max_length=20, label='名称')
    hgender = serializers.IntegerField(choices=GENDER, label='性别', required=False)
    hcomment = serializers.CharField(max_length=200, label='描述信息', allow_null=True)
