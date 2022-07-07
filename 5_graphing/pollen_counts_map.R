library(ggplot2)
library(sp)
library(raster)
library(broom)
library(tidyverse)
library(gpclib)
library(rgeos)
library(readr)
library(haven)

library(rgdal)
library(maptools)
if (!require(gpclib)) install.packages("gpclib", type="source")
gpclibPermit()


jpn2 <- getData("GADM", country = "JPN", level = 2)

jpn2_df <- tidy(jpn2, region = "NAME_2")

jpn2_df$id <- str_replace_all(jpn2_df$id, "ō", "o")
jpn2_df$id <- str_replace_all(jpn2_df$id, "Ō", "O")
jpn2_df$id <- str_replace_all(jpn2_df$id, "ū", "u")

id <- jpn2_df %>% group_by(id) %>% summarise(long = mean(long), lat = mean(lat))

oseti_tweets <- read_dta("GitHub/Twitter-Sentiment-Analysis/4_tweets_aggregated/twitter_mun_cleaned2.dta")

oseti_tweets <- oseti_tweets[!is.na(oseti_tweets$pollen_t999), ]

tweet_counts <- oseti_tweets %>% group_by(mun_id) %>% summarise(pollen = mean(pollen_t999), long = mean(mun_X), lat = mean(mun_Y))

library(geosphere)
mat <- distm(id[,c('long','lat')], tweet_counts[,c('long','lat')], fun=distVincentyEllipsoid)
id$pollen <- tweet_counts$pollen[apply(mat, 1, which.min)]

id <- subset(id, select = c(id, pollen))

df <- merge(jpn2_df, id, by = 'id')

my_breaks = c(0, 30, 100, 300, 1000, 3000)

library(scales) 

library(readxl)
pollen_station_master <- read_excel("GitHub/Twitter-Sentiment-Analysis/5_graphing/pollen_station_master.xlsx")

pollen_station_master <- subset(pollen_station_master, last_year >= 2019)

pollen_station_master$station <- "Pollen Count Station"


ggplot() + geom_polygon(data = df, aes(x = long, y = lat, group = group, fill = pollen)) + geom_point(data = pollen_station_master, aes(x = longitude, y = latitude, color = station), size=1) + labs(color = "") + theme_void() + coord_equal(xlim = c(127, 147), ylim = c(30,46)) + scale_fill_gradient(high = "#132B43", low = "#56B1F7", name = "Average Daily Pollen in 2019", labels = comma) + ggtitle("Average Daily Pollen Counts in Japan (2019)")









