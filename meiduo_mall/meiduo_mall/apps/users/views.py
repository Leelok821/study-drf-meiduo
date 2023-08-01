from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import CreateUserSerializer


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