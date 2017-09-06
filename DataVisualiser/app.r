install.packages('RPostgreSQL')
require("RPostgreSQL")

#saves the password to hide it as best as we can
 pw <- { "postgres"}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "postgres",
                 host = "localhost", port = 5432,
                 user = "postgres", password = pw)
rm(pw) # removes the password
 
# check for the cartable
dbExistsTable(con, "sprint")

