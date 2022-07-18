library(dplyr)
library(haven)
library(binsreg)
library(ggplot2)
library(bbplot)
library(ggthemes)

setwd("C:/Users/jack-/OneDrive/Documents/GitHub/Twitter-Sentiment-Analysis/4_tweets_aggregated")

df <- read_dta("./twitter_mun_cleaned2.dta")

est = binsreg(y = df$mean_oseti_score1, x = df$ln_pollen_t999, 
        w = df$temperature + df$rainfall + df$wind_speed + df$month_pref + df$dow,
        polyreg = 1,
        data = df)

result <- est$data.plot$`Group Full Sample`

fig <- ggplot() + labs(x='ln(Pollen)', y = 'Oseti Score 1') 
fig <- fig + geom_point(data=result$data.dots, aes(x=x, y=fit), color="darkblue", size=2, shape=19) 
fig <- fig + geom_line(data=result$data.poly, aes(x=x, y=fit), color='darkorange', size = 1)

fig <- fig + ggtitle("Binned Scatter Plot of Pollen vs Twitter Sentiment")
fig <- fig + theme_light()

# Display the plot
print(fig)

fig <- fig + coord_cartesian(xlim = c(2, 9), ylim = c(0.35, 0.39))


