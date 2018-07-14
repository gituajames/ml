from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from.models import kenya, checkpoint, Lan


admin.site.register(kenya, admin.GeoModelAdmin)
admin.site.register(checkpoint, LeafletGeoAdmin)
admin.site.register(Lan)