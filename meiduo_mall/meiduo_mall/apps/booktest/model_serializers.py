# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''

from rest_framework import serializers

from booktest.models import BookInfo, HeroInfo

class BookInfoModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = '__all__'

class HeroInfoModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = HeroInfo
        exclude = ('hbook',)
        

