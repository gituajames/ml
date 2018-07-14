import osgeo.ogr
shp = osgeo.ogr.Open('data/kenya.shp')
numLayers = shp.GetLayerCount()
print('shapefile contains %d layers' %numLayers)
print('')
for layerNum in range(numLayers):
	layer = shp.GetLayer(layerNum)
	spatialRef = layer.GetSpatialRef().ExportToProj4()
	numFeatures = layer.GetFeatureCount()
	print('Layer %d has spatial ref %s '%(layerNum,spatialRef))
	print('Layer %d has %d features:' %(layerNum, numFeatures))
	print('')

	for featureNum in range(numFeatures):
		feature = layer.GetFeature(featureNum)
		featureName = feature.GetField('COUNTY_NAM')
		print('Feature %d has name %s' %(featureNum,featureName))
