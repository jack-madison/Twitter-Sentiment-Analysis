import pandas as pd
import numpy as np
import math

# Import municipalities
mun_list = pd.read_csv('./5_graphing/tweet_location_map_municipality/mun_list.csv')
mun_list = mun_list[['mun_id', 'mun_X', 'mun_Y']]
mun_list.columns = ['mun_id', 'lon', 'lat']

# Import the city list
city_list = pd.read_csv("./5_graphing/tweet_location_map_municipality/map_cities.csv")

# Create a list of the map city coordinates
city_coordinates = [(x,y) for x,y in zip(city_list['lon'] , city_list['lat'])]

# Create an empty column for the lon and lat coordinates for the closest city to each tweet municipality
mun_list['closest_lon'] = np.nan
mun_list['closest_lat'] = np.nan

# For each tweet, find the closest lat and lon pair and then write that pair to the mun_X and mun_Y variables
for x in range(len(mun_list)):
    closest = min(city_coordinates, key=lambda point: math.hypot(mun_list['lat'][x]-point[1], mun_list['lon'][x]-point[0]))
    mun_list['closest_lon'][x] = closest[0]
    mun_list['closest_lat'][x] = closest[1]
    x

mun_list = mun_list[['mun_id', 'closest_lon', 'closest_lat']]
mun_list.columns = ['mun_id', 'lon', 'lat']
mun_list = pd.merge(mun_list, city_list, how = 'left', on = ["lon", "lat"])
mun_list = mun_list[['mun_id', 'city']]

mun_list.to_csv('./5_graphing/tweet_location_map_municipality/matched_cities.csv')