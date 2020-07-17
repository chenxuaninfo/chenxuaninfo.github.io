##
# Sunvasts.com
##

RecordPerformance <- function(Prod,ODate,OTime,OPrice,BS,Qty,CData,CTime,CPrice,SID,ID){
	library("RSQLite")
	appdatapath<-Sys.getenv("APPDATA")
	sqlite <- dbDriver("SQLite")
	con <- dbConnect(sqlite,paste0(appdatapath,"\\MicroBase","\\BackTest.db"))

	OTime <- sprintf('%08d',OTime)
	CTime <- sprintf('%08d',CTime)

	OTime1<- paste0(substr(OTime,1,2),":",substr(OTime,3,4),":",substr(OTime,5,6))
	CTime1<- paste0(substr(CTime,1,2),":",substr(CTime,3,4),":",substr(CTime,5,6))


	RS <- paste0("insert into Taifax(ITEM,ODate,OTime,OPrice,BorS,Number,CDate,CTime,CPrice,Comment,Tax,Fee,PID,ID) values(	'",Prod,"','",ODate,"','",OTime1,"',",OPrice,",'",BS,"',",Qty,",'",Date,"','",CTime1,"',",CPrice,",'',82,100,'",SID,"','",ID,"')")
	print(RS)
	dbGetQuery(con,RS)
	dbDisconnect(con)
}
