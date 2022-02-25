from rest_framework import serializers
from api.restapp.models import Distance


'''
    This is a serializer which will handle conversion of python native datatypes to model objects and vice versa.
'''
class DistanceSerializer(serializers.ModelSerializer):
    distance = serializers.CharField()
    class Meta:
        model = Distance
        fields = ['city1', 'city2', 'distance']
