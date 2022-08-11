# Read in the packages and custom functions from the "functions.R" file
source("functions.R")

# Read the excel file to be graphed
estimates <- read_excel("estimates.xlsx")

# Read the columns of the data frame
tp <- estimates$Estimate
cilo <- estimates$Lower
cihi <- estimates$Upper
n <- length(tp):1
nn <- n

# Set the minimum and maximum x axis values and the tick marks
### Enter seq( x axis minimum, x axis maximum, tick mark interval) ###
xx <- seq(-0.1,0.6,0.1)

# Read in the mean column from the data frame
br <- estimates$Mean

# Set the colour of the points to be plotted
colz = rep("black", length(tp))

# Read in the category and group labels
txt1 <- unique(estimates$Category)
txt2 <- estimates$Group

# Format the confidence interval data to be displayed in the table
ci <-  formatC(round(tp,2),digits=2,format="f")%&%" ("%&%formatC(round(cilo,2),digits=2,format="f")%&%","%&%formatC(round(cihi,2),digits=2,format="f")%&%")" #this makes sure lenght of character string is the same

# Specify the horizontal breaks
### Place the horizontal breaks at the half way points between each category ###
lz <- c(4.5, 8.5, 10.5, 14.5, 16.5)

# Specify the placement of the category labels
### Place the category labels at the midpoint of each category (i.e. first category has 4 elements so place at 2.5)###
cat_locs <- c(2.5, 6.5, 9.5, 12.5, 15.5, 18.5)

# Plot

#Specify the output name and figure dimensions
### If the figure is too spaced out or squashed vertically, change the height variable ###
pdf(file="./figure.pdf",width=9,height=6,useDingbats = F)

# Set the margins
par(mgp=c(2,0.8,0),mar=c(5,4,4,3),lend=1)

# Set the plot options
### To change the x axis label, change the xlab text ###
### In order to have the graph portion of the table be scaled correctly you will have to adjust the xlim() options ###
### If the graph is too narrow, reduce the range of the xlim. If the graph is too wide, increase the xlim range ###
plot(1,type="n",xlim=c(-1.1,0.8),ylim=c(1,dim(estimates)[1]),axes=F,ylab="",xlab="% change in monthly suicide rate")

# More plot options
abline(v=xx,lwd=0.5,col="grey",lty=2)
abline(v=0,lwd=0.5)
segments(cilo,nn,cihi,nn)
points(tp,nn,pch=21,bg=colz,cex=1.2)
abline(h=lz,lwd=0.75,lty=1,col="grey")
axis(1,at=xx,labels=xx)

# Place the text columns
### You will have to play around with the first number in each of the text() options ###
### in order to place the columns correctly. Use this in conjunction with the xlim option ###
### above to space the chart elements correctly. ###
text(-1.16, cat_locs, txt1, cex=0.65, pos=4)
text(-0.75,nn,txt2,cex=0.65,pos=4)
text(-0.5,nn,format(estimates$N,big.mark = ","),pos=4,cex=0.65)
text(-0.25,nn,formatC(round(br,2),digits=2,format="f"),cex=0.65,pos=4)
text(0.75,nn,ci,cex=0.65)

dev.off()
