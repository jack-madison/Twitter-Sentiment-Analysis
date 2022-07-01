library(dplyr)
library(haven)
library(binsreg)
library(ggplot2)
library(bbplot)

setwd("C:/Users/jack-/OneDrive/Documents/GitHub/Twitter-Sentiment-Analysis/4_tweets_aggregated")

df <- read_dta("./twitter_mun_cleaned2.dta")

est = binsreg(y = df$mean_oseti_score1, x = df$ln_pollen_t999, 
        w = df$temperature + df$rainfall + df$wind_speed,
        polyreg = 1,
        data = df)

result <- est$data.plot$`Group Full Sample`

windowsFonts(Helvetica = "Calibri")

# Create the figure to plot
fig <- ggplot() + labs(x='ln(Pollen)', y = 'Oseti Score 1') 
fig <- fig + geom_point(data=result$data.dots, aes(x=x, y=fit), color="blue", size=2, shape=19) 
fig <- fig + theme_light()
fig <- fig + geom_line(data=result$data.poly, aes(x=x, y=fit), color="blue", size=0.5)

# Display the plot
print(fig)