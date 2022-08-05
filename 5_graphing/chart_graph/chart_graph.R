source("functions.R")
library(tidyverse)
library(readxl)

estimates <- read_excel("estimates.xlsx")

tp <- estimates$Estimate
cilo <- estimates$Lower
cihi <- estimates$Upper
n <- length(tp):1
xx <- seq(-0.1,0.6,0.1)

br <- estimates$Mean

nn <- n

colz = rep("black", length(tp))

txt1 <- unique(estimates$Category)
txt2 <- estimates$Group

ci <-  formatC(round(tp,2),digits=2,format="f")%&%" ("%&%formatC(round(cilo,2),digits=2,format="f")%&%","%&%formatC(round(cihi,2),digits=2,format="f")%&%")" #this makes sure lenght of character string is the same

lz <- c(4.5, 8.5, 10.5, 14.5, 16.5)  #horizontal break lines to divide up the different subgroups

cat_locs <- c(18.5, 15.5, 12.5, 9.5, 6.5, 2.5)

# Plot

pdf(file="./figure.pdf",width=9,height=6,useDingbats = F)

par(mgp=c(2,0.8,0),mar=c(5,4,4,3),lend=1)

plot(1,type="n",xlim=c(-1.1,0.8),ylim=c(1,dim(estimates)[1]),axes=F,ylab="",xlab="% change in monthly suicide rate")

abline(v=xx,lwd=0.5,col="grey",lty=2)
abline(v=0,lwd=0.5)
segments(cilo,nn,cihi,nn)

points(tp,nn,pch=21,bg=colz,cex=1.2)

abline(h=lz,lwd=0.75,lty=1,col="grey") #with subgroup ordering
axis(1,at=xx,labels=xx)

text(-1.16, cat_locs, txt1, cex=0.65, pos=4)
text(-0.75,nn,txt2,cex=0.65,pos=4)
text(-0.5,nn,format(estimates$N,big.mark = ","),pos=4,cex=0.65)  #this adds comma in number
text(-0.25,nn,formatC(round(br,2),digits=2,format="f"),cex=0.65,pos=4)
text(0.75,nn,ci,cex=0.65)

dev.off()
