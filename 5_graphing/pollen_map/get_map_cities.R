library(tidyverse)
library(readr)
library(sp)
library(raster)
library(broom)
library(ggmap)
library(rstudioapi)
library(geosphere)
library(rgeos)

register_google(key = "AIzaSyBYSCM6Y1kaV5m_Gb1YpO11pGQiEU0_fLU")

# Get the geodata from GADM
jpn2 <- getData("GADM", country = "JPN", level = 2)
jpn2_df <- tidy(jpn2, region = "NAME_2")
rm(jpn2)

# Create a dataframe with the names of each of the cities from jpn2_df
city_df <- data.frame(unique(jpn2_df$id))
colnames(city_df) <- c("city")
city_df$city_japan <- paste(city_df$city, ", Japan")

# For each of the cities get the lat and lon from the google maps API
for (i in 1:nrow(city_df)) {
  result <- geocode(city_df$city_japan[i])
  city_df$lon[i] <- as.numeric(result[1])
  city_df$lat[i] <- as.numeric(result[2])
}

# The google maps API was unable to find the lat and lon for 4 cities so:

# Set Asakura lat manually
city_df$lon[65] <- as.numeric(130.66565696500018)
city_df$lat[65] <- as.numeric(33.423355345642065)

# Set Fuji Manually
city_df$lon[154] <- as.numeric(138.67624139992301)
city_df$lat[154] <- as.numeric(35.1615654218984)

# Set Midori Manually
city_df$lon[765] <- as.numeric(139.2732842846065)
city_df$lat[765] <- as.numeric(36.43298967377905)

# Set Sakura Manually
city_df$lon[1170] <- as.numeric(140.2240090321607)
city_df$lat[1170] <- as.numeric(35.72362777755255)

# Drop the city_japan column as it is no longer needed
city_df <- subset(city_df, select = c("city", "lon", "lat"))

# Output the list of cities to a csv
write.csv(city_df, "map_cities.csv", row.names = FALSE)
