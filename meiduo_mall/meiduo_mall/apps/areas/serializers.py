from rest_framework import serializers
from areas.models import Areas

# class AreasSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Areas
#         fields = ['id', 'name']

# class SubsSerializer(serializers.ModelSerializer):

#     subs = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

#     class Meta:
#         model = Areas
#         fields = '__all__'


class AreasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Areas
        fields = ('id', 'name')

class SubsSerializers(serializers.ModelSerializer):
    subs = AreasSerializer(many=True, read_only=True)

    class Meta:
        model = Areas
        fields = ('id', 'name', 'subs')