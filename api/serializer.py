from rest_framework import serializers
from celes_obj.models import CelestialObject

class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialObject
        fields = '__all__'