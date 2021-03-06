"""
Karina Ionkina
SoftDev1 pd07
HW09 -- All About That Base
2017-10-15
"""
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from csv import DictReader

"""
 useless chunk of code because CSV files do not preserve type

def get_type(x):
    if type(x) is int:
        return 'INTEGER'
    if type(x) is str or type(x) is char:
        return 'TEXT'
    if type(x) is float or type(x) is double:
        return 'REAL'
    else:
        return 'BLOB'
"""

def populate(filename, table_name):
    ''' Parse CSV file with DictReader

    :param filename: Insert file
    '''
    f="discobandit.db"

    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        dicts = []
        for dict in reader:
            dicts.append(dict)
        for dict in dicts:
            s = "INSERT INTO " + table_name + " VALUES (" 
            for key in dict.keys():
                s += "'" + dict[key] + "'" + ","
            s = s[: len(s) - 1] + ")"
            c.execute(s)
            db.commit() #save changes
    db.close()  #close database



f="discobandit.db"    
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
command1 = "CREATE TABLE " + 'Peepz' + " (Age BLOB, Name BLOB, ID BLOB)"
c.execute(command1)    
db.commit() #save changes
db.close()  #close database
populate("peeps.csv", "Peepz")

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
command1 = "CREATE TABLE " + 'coursez'+ " (Code BLOB, ID BLOB, Mark BLOB)"
c.execute(command1)
db.commit() #save changes
db.close()  #close database

populate("courses.csv", "coursez")


