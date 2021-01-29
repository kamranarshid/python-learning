#!/usr/bin/env python
# coding: utf-8

import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'Host'
database = 'DATABASE'
username = 'USER'
password = 'PASSWORD'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

# Sample select query
cursor.execute("SELECT * from users;")

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()

if cursor.rowcount < 3:
    print("Records more than 3")
else:
    print("ok")
