#!/usr/bin/python

hostname = 'localhost'
username = 'iuser'
password = 'pass'
database = 'ingredients'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    console.log(cur)

    cur.execute( "SELECT name FROM ingredients" )

    for name in cur.fetchall() :
        print(name)


print("Using psycopg2…")
import psycopg2
conn_string = "host='localhost' dbname='ingredients' user='iuser' password='pass'"
myConnection = psycopg2.connect( conn_string )
print(myConnection)
doQuery( myConnection )
myConnection.close()

# print("Using PyGreSQL…")
# import pgdb
# myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
# doQuery( myConnection )
# myConnection.close()