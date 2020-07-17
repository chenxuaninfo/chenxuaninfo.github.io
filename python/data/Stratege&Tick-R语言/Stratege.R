source("Function.R")

date="20170508"

I020<-read.csv(paste0("Futures_",date,"_I020.csv"),header=FALSE)
colnames(I020)<-c("INFO_TIME","MATCH_TIME","PROD","ITEM","PRICE","QTY","AMOUNT","MATCH_BUY_CNT","MATCH_SELL_CNT")

ID <- "Trader1"
SID <- "TradeTest"
Date <- paste0(substr(date,1,4),"-",substr(date,5,6),"-",substr(date,7,8))
Prod <- "TXFD7"
A01 <- I020[c(1,4,5)]	
A02 <- subset(A01, INFO_TIME>=as.numeric(09000000) & INFO_TIME<=as.numeric(11000000)) 

OrderTime <- A02[1,]$INFO_TIME
OrderPrice <- A02[1,]$PRICE

CoveryTime <- A02[nrow(A02),]$INFO_TIME
CoveryPrice <- A02[nrow(A02),]$PRICE

cat("BUY TIME:",OrderTime,"PRICE:",OrderPrice,"COVERY TIME:",CoveryTime,"C_PRICE:",CoveryPrice,"PROFIT",CoveryPrice-OrderPrice,'\n')
RecordPerformance(Prod,Date,OrderTime,OrderPrice,"B",1,Date,CoveryTime,CoveryPrice,SID,ID)