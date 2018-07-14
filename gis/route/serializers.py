from rest_framework import serializers
from .models import Lan, kenya

class LanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lan
        fields = ('id', 'name', 'paradigm')

class kenyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kenya
        fields = ('unit_area', 'unit_perim', 'district', 'count', 'county_nam', 'code', 'geom')