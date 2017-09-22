#!/usr/bin/Rscript
#install.packages('RPostgreSQL')
require("RPostgreSQL")

rm(list = ls())      # Clear all variables
graphics.off()       # Close graphics windows

#saves the password to hide it as best as we can
 pw <- { "postgres"}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "postgres",
                 host = "localhost", port = 5011,
                 user = "postgres", password = pw)
rm(pw) # removes the password
 
# check if table if found
stopifnot(dbExistsTable(con, "sprint"))

#if it exists we connect to the table and get the values
sprint_value <- dbReadTable(con, "sprint")
sp_committed <- sprint_value$story_points_committed
sp_finished <- sprint_value$story_points_finished
sprints_amount <- length(sp_committed)

##we manipulate data to fit our first graph
mat <- matrix(list(), nrow=2, sprints_amount)
for (i in 1:sprints_amount){
	mat[ ,i] = c(sp_committed[i],sp_finished[i])
}
x11()
attach(mtcars)
par(mfrow=c(2,1))
bp = barplot(rbind(sp_finished, sp_committed), main="Sprints overview", ylab="Story points", beside=TRUE, col=c("blue", "green"))
plot(sp_finished - sp_committed,main='Story points surplus', type = 'o')

Sys.sleep(99999999999)



