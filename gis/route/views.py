from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets
from . models import checkpoint, kenya, Lan
from .serializers import LanSerializer, kenyaSerializer

class LanView(viewsets.ModelViewSet):
    queryset = Lan.objects.all()
    serializer_class =  LanSerializer


class LanView(viewsets.ModelViewSet):
    queryset = kenya.objects.all()
    serializer_class =  kenyaSerializer

def home(request):
    point = checkpoint.objects.all()
    j_son = serialize('geojson', point, fields=('id', 'name', 'location'))
    return render(request, 'home.html', {'point':point, 'j_son':j_son})


def shpPoint(request):
  points = kenya.objects.kml()
  return render_to_kml("placemarks.kml", {'points': points})