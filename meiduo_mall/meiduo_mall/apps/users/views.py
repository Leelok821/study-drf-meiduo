from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer


# # 用APIView实现

# class UserView(APIView):
    
#     def post(self, request):
#         # 获取前端传递数据
#         font_data = request.data
#         # 将数据传递给序列化器进行反序列化
#         serilizer = UserSerializer(data=font_data)
#         # 数据验证,返回true或者false
#         data = serilizer.is_valid()
#         if data:
#         # 保存数据
#             serilizer.save()
#             data1 = serilizer.validated_data
#             data2 = serilizer.data
#             print(f'{data1}\n{data2}')
#             return Response(f'{data1}\n{data2}',status=status.HTTP_201_CREATED)
#         else:
#             return Response('参数错误',status=status.HTTP_406_NOT_ACCEPTABLE)

"""
用GenericAPIView实现列表视图
"""
class UserView(GenericAPIView):

    # 列表视图
    queryset = User.objects.all()