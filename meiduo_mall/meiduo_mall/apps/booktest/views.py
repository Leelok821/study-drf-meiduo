from django.shortcuts import render

# Create your views here.


from booktest.models import BookInfo, HeroInfo
from rest_framework.response import Response
from django.http import HttpResponse
from booktest.serializers import BookInfoSerializer

def add_book(request):
    b = BookInfo(btitle='天龙八部',bpub_date='2023-1-21')
    b.save()
    return HttpResponse('111')

def get_book(request):
    """
    序列化单个对象
    """
    # 获取单个对象
    book = BookInfo.objects.get(id=7)

    # 获取书籍
    # b = BookInfo.objects.all()
    # print(f'===={b.btitle}')
    # 序列化
    ser = BookInfoSerializer(instance=book)
    # 返回序列化数据
    print(ser.data)
    return HttpResponse(ser.context)

def add_hero(request):
    hero = HeroInfo(hname='刘备',hbook=7)
    hero.save()
    return HttpResponse('111')