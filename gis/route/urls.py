from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from djgeojson.views import GeoJSONLayerView

router = routers.DefaultRouter()
router.register('Lan', views.LanView)

urlpatterns = [
    path('home', views.home, name='home'),
    path('home1', views.shpPoint, name='home1'),
    path('api', include(router.urls)),
    path('kenya', include(router.urls)),
    # path('data', GeoJSONLayerView.as_view(model=checkpoint), name='data')

]