library(tidyverse)
library(haven)
library(readr)
library(dplyr)

library(sp)
library(raster)
library(broom)
library(gpclib)
library(rgeos)
library(rgdal)
library(maptools)
library(viridis)

pollen_mun_20082019 <- read_dta("pollen_mun_20082019.dta")

cities <- read_csv("matched_cities.csv")

pollen <- merge(x = pollen_mun_20082019, y = cities, by = "mun_id", all.x = TRUE)

pollen <- pollen %>% group_by(city) %>% summarise(avg_pollen = mean(pollen, na.rm = TRUE))

names(pollen)[names(pollen) == 'city'] <- 'id'

jpn2 <- getData("GADM", country = "JPN", level = 2)
jpn2_df <- tidy(jpn2, region = "NAME_2")

jpn2_df <- left_join(jpn2_df, pollen)

ggplot() +
  geom_polygon(data = jpn2_df,
               aes(x = long, y = lat, group = group, fill = avg_pollen)) +
  labs(x = "", y = "") + ggtitle("Average Municipality Level Pollen in Japan (2008 to 2019)") + 
  coord_equal() + scale_fill_viridis(name = "Average Daily Pollen", trans = 'log') +
  theme_void() + theme(legend.position = c(0.85, 0.2))
