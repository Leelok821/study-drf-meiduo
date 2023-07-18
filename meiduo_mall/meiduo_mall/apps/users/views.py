from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.serializers import Serializer

class UserView(APIView):

    serilizer = Serializer()
    
    def post(self, request):
        pass