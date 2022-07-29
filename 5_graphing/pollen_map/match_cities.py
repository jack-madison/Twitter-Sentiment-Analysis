import pandas as pd
import numpy as np
import math

# Import municipalities
mun_list = pd.read_csv('./5_graphing/pollen_map/mun_list.csv')
mun_list = mun_list[['mun_id', 'mun_X', 'mun_Y']]
mun_list.columns = ['mun_id', 'lon', 'lat']

# Import the city list
city_list = pd.read_csv("./5_graphing/pollen_map/map_cities.csv")

# Create a list of the map city coordinates
mun_coordinates = [(x,y) for x,y in zip(mun_list['lon'] , mun_list['lat'])]

# Create an empty column for the lon and lat coordinates for the closest city to each tweet municipality
city_list['closest_lon'] = np.nan
city_list['closest_lat'] = np.nan

# For each tweet, find the closest lat and lon pair and then write that pair to the mun_X and mun_Y variables
for x in range(len(city_list)):
    closest = min(mun_coordinates, key=lambda point: math.hypot(city_list['lat'][x]-point[1], city_list['lon'][x]-point[0]))
    city_list['closest_lon'][x] = closest[0]
    city_list['closest_lat'][x] = closest[1]
    x

city_list = city_list[['city', 'closest_lon', 'closest_lat']]
city_list.columns = ['city', 'lon', 'lat']
city_list = pd.merge(city_list, mun_list, how = 'left', on = ["lon", "lat"])
city_list = city_list[['mun_id', 'city']]

city_list.to_csv('./5_graphing/pollen_map/matched_cities.csv', index = False)