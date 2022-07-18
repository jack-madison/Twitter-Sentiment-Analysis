library(tidyverse)
library(readr)
library(sp)
library(raster)
library(broom)
library(gpclib)
library(rgeos)
library(rgdal)
library(maptools)

oseti_tweets_mun_2019 <- read_csv("oseti_tweets_mun_2019.csv")
oseti_tweets_mun_2018 <- read_csv("oseti_tweets_mun_2018.csv")
oseti_tweets_mun_2017 <- read_csv("oseti_tweets_mun_2017.csv")

tweets <- rbind(oseti_tweets_mun_2019, oseti_tweets_mun_2018, oseti_tweets_mun_2017)

rm(oseti_tweets_mun_2019)
rm(oseti_tweets_mun_2018)
rm(oseti_tweets_mun_2017)

cities <- read_csv("matched_cities.csv")

tweets <- merge(x = tweets, y = cities, by = "mun_id", all.x = TRUE)

tweet_counts <- tweets %>% group_by(city) %>% summarise(tweet_count = sum(tweet_count))
tweet_counts <- rename(tweet_counts, id = city)


jpn2 <- getData("GADM", country = "JPN", level = 2)
jpn2_df <- tidy(jpn2, region = "NAME_2")

id <- unique(jpn2_df$id)

df_city <- data.frame(id)





df <- merge(jpn2_df, tweet_counts, by = 'id', )
df[is.na(df)] <- 0

library(scales) 

ggplot() + geom_polygon(data = jpn2_df, aes(x = long, y = lat, group = group, fill = id)) + theme_void() + theme(legend.position = "none")

ggplot() + geom_polygon(data = df, aes(x = long, y = lat, group = group, fill = id)) + theme_void() + theme(legend.position = "none")






