from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework import status
from users.models import User, Address
from users.serializers import CreateUserSerializer, UserDetailSerializer, EmailSerializer, AddressSerializer
from rest_framework.permissions import IsAuthenticated
from meiduo_mall.apps.users import constants



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

class AddressViewSet(CreateModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.request.user.addresses.filter(is_deleted=False)

    # GET /addresses/
    def list(self, request, *args, **kwargs):
        """用户地址列表数据"""
        seria = self.get_serializer(self.get_queryset, many=True)
        res = {
            'message':'ok',
            'addresses': seria.data,
        }
        return Response(res, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """创建用户地址"""
        # 校验用户地址是否超限
        count = request.user.addresses.count()
        if count <= constants.USER_ADDRESS_COUNTS_LIMIT:
            return Response({'messgae':'超过上限'}, status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    # # /addresses/
    # def create(self, request, *args, **kwargs):
    #     # 判断用户有没有超过20个地址
    #     count = self.request.user.addresses.count()  # self.request.user ？？？
       
    #     if count >= constants.USER_ADDRESS_COUNTS_LIMIT:
    #         return Response({'message':'保存地址超过上限'}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().create(request, *args, **kwargs)
    
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
