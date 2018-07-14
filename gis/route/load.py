import os
from django.contrib.gis.utils import LayerMapping
from . models import kenya

kenya_mapping = {
    'unit_area': 'UNIT_AREA',
    'unit_perim': 'UNIT_PERIM',
    'district': 'DISTRICT',
    'count': 'COUNT',
    'county_nam': 'COUNTY_NAM',
    'code': 'CODE',
    'geom': 'MULTIPOLYGON',
}


kenya_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'kenya.shp'),
)

def run(verbose=True):
	lm = LayerMapping(kenya, kenya_shp, kenya_mapping,transform=False,encoding='iso-8859-1',)
	lm.save(strict=True, verbose=verbose)