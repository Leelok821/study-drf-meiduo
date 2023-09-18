from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from areas.models import Areas
from areas.serializers import *
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# Create your views here.


# class AreaViewSet(ReadOnlyModelViewSet):

#     def get_queryset(self):
#         if self.action == 'list':
#             return Areas.objects.filter(parent=None)
#         else:
#             return Areas.objects.all()
    
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return AreasSerializer
#         else:
#             return SubsSerializer


# class ListAreaView(APIView):

#     permission_classes = []

#     def get(self, request):
#         # 查询数据
#         qs = Areas.objects.filter(parent=None)
#         # 序列化数据
#         seria = AreasSerializer(instance=qs, many=True)
#         # 响应
#         return Response(seria.data)

# class SubsAreaView(APIView):

#     permission_classes = []

#     def get(self, request, id):
#         obj = Areas.objects.get(pk=id)
#         seria = SubsSerializers(instance=obj)
#         return Response(seria.data)

# class ListAreaView(GenericAPIView):
#     queryset = Areas.objects.filter(parent=None)
#     serializer_class = AreasSerializer
#     permission_classes = []

#     def get(self, request):
#         # 查询数据
#         qs = self.get_queryset()
#         # 序列化
#         seria = self.get_serializer(qs, many=True)
#         # 响应
#         return Response(seria.data)

# class SubsAreaView(GenericAPIView):
#     queryset = Areas.objects
#     serializer_class = SubsSerializers
#     permission_classes = []
#     lookup_field = 'id'

#     def get(self, request, id):
#         # 查询数据
#         qs = self.get_object()
#         # 序列化
#         seria = self.get_serializer(qs)
#         # 响应
#         return Response(seria.data)

# class ListAreaView(GenericAPIView, ListModelMixin):
#     queryset = Areas.objects.filter(parent=None)
#     serializer_class = AreasSerializer
#     permission_classes = []

#     def get(self, request):
#         return self.list(self, request)


# class SubsAreaView(GenericAPIView, RetrieveModelMixin):
#     queryset = Areas.objects.all()
#     serializer_class = SubsSerializers
#     permission_classes = []
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(self, request, id)





# class ListAreaView(ListAPIView):
#     queryset = Areas.objects.filter(parent=None)
#     serializer_class = AreasSerializer

# class SubsAreaView(RetrieveAPIView):
#     queryset = Areas.objects.all()
#     serializer_class = SubsSerializers()


# class ListSubsAreaViewSet(ViewSet):
    
#     def list(self, request):
#         qs = Areas.objects.filter(parent=None)
#         seria = AreasSerializer(qs, many=True)
#         return Response(seria.data)
    
#     def retrieve(self, request, id):
#         object = Areas.objects.get(pk=id)
#         seria = SubsSerializers(object)
#         return Response(seria.data)

# class ListSubsAreaViewSet(GenericViewSet):
#     lookup_field = 'id'
    
#     def get_queryset(self):
#         if self.action == 'list':
#             return Areas.objects.filter(parent=None)
#         else:
#             return Areas.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return AreasSerializer
#         if self.action == 'retrieve':
#             return SubsSerializers

#     def list(self, request):
#         qs = self.get_queryset()
#         seria = self.get_serializer(qs, many=True)
#         return Response(seria.data)
    
#     def retrieve(self, request, id):
#         object = self.get_object()
#         seria = self.get_serializer(object)
#         return Response(seria.data)

class ListSubsAreaViewSet(CacheResponseMixin, ReadOnlyModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return AreasSerializer
        if self.action == 'retrieve':
            return SubsSerializers
    
    def get_queryset(self):
        if self.action == 'list':
            return Areas.objects.filter(parent=None)
        else:
            return Areas.objects.all()