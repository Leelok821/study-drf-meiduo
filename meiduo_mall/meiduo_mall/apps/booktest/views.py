from django.shortcuts import render

# Create your views here.


from booktest.models import BookInfo, HeroInfo
from rest_framework.response import Response
from django.http import HttpResponse
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from booktest.model_serializers import BookInfoModelSerializers, HeroInfoModelSerializers

from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework import status
from rest_framework.viewsets import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

"""API VIEW"""

class BookListView(APIView):

    def get(self, request):
        # 查询所有书籍
        books = BookInfo.objects.all()
        # 序列化
        seria = BookInfoModelSerializers(books, many=True)
        return Response(seria.data)
    
    def post(self, request):
        # 获取前端数据
        data_front = request.data
        # 反序列化
        seria = BookInfoModelSerializers(data=data_front)
        # 校验
        errors = seria.is_valid()
        if errors:
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        
class BookDetailView(APIView):

    def get(self, request, id):
        # 查询对象
        try:
            book = BookInfo.objects.get(id=id)
            seria = BookInfoModelSerializers(book)
        except BookInfo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(seria.data, status.HTTP_200_OK)
    
    def put(self, reuqest, id):
        # 查询对象,若对象不存在抛出异常
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 获取请求数据
        data_front = reuqest.data
        # 序列化数据
        seria = BookInfoModelSerializers(book, data=data_front)
        # 校验
        seria.is_valid(raise_exception=True)
        # 保存数据
        seria.save()
        return Response(seria.data, status.HTTP_200_OK)



    
"""GenericAPIView"""


class BookInfoGenericApiView(GenericAPIView):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers

    def get(self, request):
        queryset = self.get_queryset()
        seria = self.get_serializer(queryset, many=True)
        return Response(seria.data)
    
    def post(self, request):
        # 获取前端数据
        data_front = request.data
        # 获取序列化器
        seria = self.get_serializer(data=data_front)
        # 校验
        seria.is_valid(raise_exception=True)
        # 入库
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class BookDetailGenericAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'

    def get(self, request, id):
        book = self.get_object()
        seria = self.get_serializer(book)
        return Response(seria.data)

    def put(self, request, id):
        book = self.get_object()
        data_front = request.data
        seria = self.get_serializer(book, data=data_front)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)

"""GenericAPIView + 各种mixin"""


class BookInfoGenericApiView(GenericAPIView, ListModelMixin, CreateModelMixin):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class BookDetailGenericAPIView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)
    

"""三级视图"""


class BookInfoGenericApiView2(CreateAPIView, ListAPIView):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers

class BookDetailGenericApiView2(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'


"""视图集ViewSet"""

class BookViewSet(ViewSet):
    
    def list(self, request):
        qs = BookInfo.objects.all()
        seria = BookInfoModelSerializers(qs, many=True)
        return Response(seria.data)
    
    def retrieve(self, request, id):
        qs = BookInfo.objects.all()
        book = get_object_or_404(qs, id=id)
        seria = BookInfoModelSerializers(book)
        return Response(seria.data)

"""GenericViewSet"""

class BookGenericViewSet(GenericViewSet):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'

    def list(self, request):
        qs = self.get_queryset()
        seria = self.get_serializer(qs, many=True)
        return Response(seria.data)
    
    def retrieve(self, request, id):
        qs = self.get_queryset()
        book = get_object_or_404(qs, id=id)
        seria = self.get_serializer(book)
        return Response(seria.data)
    
    def create(self, request):
        data = request.data
        seria = self.get_serializer(data=data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status.HTTP_201_CREATED)
    
    def update(self, request, id):
        data = request.data
        qs = self.get_queryset()
        book = get_object_or_404(qs, id=id)
        seria = self.get_serializer(book, data=data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, id):
        qs = self.get_queryset()
        book = get_object_or_404(qs, id=id)
        book.delete()
        return Response(status.HTTP_200_OK)

"""ReadOnlyModelViewSet"""

class BookReadOnlyModelViewSet(ReadOnlyModelViewSet):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'

"""ReadOnlyModelViewSet"""

class BookModelViewSet(ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializers
    lookup_field = 'id'