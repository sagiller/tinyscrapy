#encoding: utf-8
import MySQLdb

HOST = "127.0.0.1"
PORT = 27017

db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                     user="root", # your username
                      passwd="123456", # your password
                      db="test") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM test")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]


