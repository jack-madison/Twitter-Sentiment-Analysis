library(ggplot2)
library(sp)
library(raster)
library(broom)
library(tidyverse)
library(gpclib)
library(rgeos)
library(readr)

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

oseti_tweets_mun_2017 <- read_csv("oseti_tweets_mun_2017.csv")
oseti_tweets_mun_2018 <- read_csv("oseti_tweets_mun_2018.csv")
oseti_tweets_mun_2019 <- read_csv("oseti_tweets_mun_2019.csv")

oseti_tweets <- rbind(oseti_tweets_mun_2017, oseti_tweets_mun_2018, oseti_tweets_mun_2019)

tweet_counts <- oseti_tweets %>% group_by(mun_id) %>% summarise(tweet_count = sum(tweet_count), long = mean(mun_X), lat = mean(mun_Y))

library(geosphere)
mat <- distm(id[,c('long','lat')], tweet_counts[,c('long','lat')], fun=distVincentyEllipsoid)
id$tweets <- tweet_counts$tweet_count[apply(mat, 1, which.min)]

id <- subset(id, select = c(id, tweets))

df <- merge(jpn2_df, id, by = 'id')

df$ln_tweets <- log(df$tweets)

my_breaks = c(100, 10000, 1000000)

library(scales) 

library(viridis)
ggplot() + geom_polygon(data = df, aes(x = long, y = lat, group = group, fill = tweets)) + theme_void() + theme(legend.position = c(.85, .35), plot.title = element_text(hjust = 0.2, vjust = -30)) + coord_equal(xlim = c(127, 147), ylim = c(30,46)) + scale_fill_viridis(name = "Total Tweets", trans = "log", labels = comma, breaks = my_breaks ) + ggtitle("Geographic Distribution of Tweets in Japan (2017 to 2019)")









