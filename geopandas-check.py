"""
geopandas-check.py
Spring 2023 PJW

Plot the boundary of Syracuse as a quick check to verify that geopandas 
is installed correctly.
"""

#  Import the modules we'll need

import geopandas as gpd
import matplotlib.pyplot as plt

#  Read the shapefile for the Census boundary of Syracuse. If this 
#  doesn't trigger an error, everything is installed OK.

syr = gpd.read_file("tl_2016_36_place-syracuse.zip")

#  Say a little about the GeoDataFrame and draw a map for good measure.

print('Features found:',len(syr))

fig1,ax1 = plt.subplots()
syr.plot(ax=ax1)
ax1.axis('off')
fig1.tight_layout()
fig1.savefig('geopandas-check.png')

print('Map saved')
