"""
geopandas-check.py
Spring 2023 PJW

Plot the boundary of Syracuse as a quick check to verify that geopandas
is installed correctly.
"""

#  Import the modules we'll need

import geopandas as gpd
import matplotlib.pyplot as plt

#  Set the default plot resolution

plt.rcParams['figure.dpi'] = 300

#  Read the shapefile for the Census boundary of Syracuse. If this
#  doesn't trigger an error, everything is installed OK.

syr = gpd.read_file("tl_2016_36_place-syracuse.zip")

#  Say a little about the GeoDataFrame

print('Features found:',len(syr))
print('Attributes found:',list(syr.columns))

#  Now plot it

fig1,ax1 = plt.subplots()
fig1.suptitle('City of Syracuse')
syr.plot(color='xkcd:lightblue',ax=ax1)
syr.boundary.plot(color='gray',linewidth=1,ax=ax1)
ax1.axis('off')
fig1.tight_layout()
fig1.savefig('geopandas-check.png')

print('Map saved')
