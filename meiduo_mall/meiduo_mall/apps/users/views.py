from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import CreateUserSerializer, UserDetailSerializer, EmailSerializer
from rest_framework.permissions import IsAuthenticated

"""使用genericapiview"""

# class UserView(GenericAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer()

#     def post(self, request):
#         data = request.data
#         seria = self.get_serializer(data=data)
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(seria.data, status.HTTP_201_CREATED)

"""使用createapiview"""

class UserView(CreateAPIView):

    serializer_class = CreateUserSerializer

class UserNameCountView(APIView):

    def get(self, request, user_name):
        user_count = User.objects.filter(username=user_name).count()
        return Response({'username':user_name, 'count': user_count})

class MobileCountView(APIView):

    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()
        return Response({'mobile':mobile, 'count': count})


class UserDetailView(RetrieveAPIView):

    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user

class EmailView(UpdateAPIView):

    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class VerifyEmailView(APIView):
    """验证邮箱"""
    # authentication_classes = []
    permission_classes = []

    def get(self, request):
        # 获取token参数
        token = request.query_params.get('token')
        if not token:
            return Response({'message':'缺少token'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 验证token参数：提取user
        user = User.check_verify_email_token(token)
        if not user:
            return Response({'message':'无效的token'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 修改用户的email_active为True，完成验证
        user.email_active = True
        user.save()
        return Response({'message': 'OK'})