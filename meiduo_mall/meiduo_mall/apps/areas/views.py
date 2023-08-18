from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from areas.models import Areas
from areas.serializers import AreasSerializer, SubsSerializer
# Create your views here.


class AreaViewSet(ReadOnlyModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Areas.objects.filter(parent=None)
        else:
            return Areas.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AreasSerializer
        else:
            return SubsSerializer
