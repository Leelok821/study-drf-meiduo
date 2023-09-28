
from rest_framework.views import APIView
from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.db.models.query import QuerySet



'''
ApiView:
    * 

'''

class BookListApiView(APIView):

    def get(self, request):
        """查"""
        qs = BookInfo.objects.all()
        seria = BookInfoSerializer(qs, many=True)
        return Response(seria.data)
    
    def post(self, request):
        """增"""
        request_data = request.data
        seria = BookInfoSerializer(data=request_data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)

class BookInfoApiView(APIView):

    def get(self, request, id):
        obj = BookInfo.objects.get(id=id)
        seria = BookInfoSerializer(obj)
        return Response(seria.data)
    
    def put(self, request, id):
        obj = BookInfo.objects.get(id=id)
        req_data = request.data
        seria = BookInfoSerializer(obj, req_data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)
    
    def delete(self, request, id):
        BookInfo.objects.get(id=id).delete()
        return Response({"message":"删除成功"})

"""
GenerateApiView
    * 添加了常用的属性和方法
        * 属性
            * queryset
        * 方法
            * .get_queryset()
"""

class BookListGenericAPIView(GenericAPIView):

    queryset = BookInfo.objects
    serializer_class = BookInfoSerializer

    def get(self, request):
        qs = self.get_queryset()
        seria = self.get_serializer(qs, many=True)
        return Response(seria.data)
    
    def post(self, request):
        