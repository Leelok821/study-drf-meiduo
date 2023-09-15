from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from areas.models import Areas
from areas.serializers import *
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


class ListAreaView(APIView):

    permission_classes = []

    def get(self, request):
        # 查询数据
        qs = Areas.objects.filter(parent=None)
        # 序列化数据
        seria = AreasSerializer(instance=qs, many=True)
        # 响应
        return Response(seria.data)

class SubsAreaView(APIView):

    permission_classes = []

    def get(self, request, id):
        obj = Areas.objects.get(pk=id)
        seria = SubsSerializers(instance=obj)
        return Response(seria.data)