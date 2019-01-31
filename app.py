import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv('data.txt')

# creating the map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start=5, tiles="Mapbox bright")

# function to group elevation by colour according to height
def range(elev):
    if (elev < 1000):
        return ('green')
    elif (1000 <= elev < 3000):
        return ('orange')
    else:
        return ('red')

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

# adding additional things to map
# coordinates_array = [[-26.2041,28.0473], [-33.9249,18.4241], [-29.0852,26.1596]]
lat = data['LAT']
long = data['LON']
elevation = data['ELEV']

for lat, long, elevation in zip(lat, long, elevation):
    folium.CircleMarker(location=[lat, long], radius=9, popup=str(elevation), fill_color=range(elevation), color="gray", fill_opacity=0.9).add_to(marker_cluster)

# saving map.html
map.save('map.html')