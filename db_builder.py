import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


