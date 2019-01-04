#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('testdb')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data

    cur.execute('select * from yves order by 1,2')
    rows = cur.fetchall()
    for row in rows:
        print row
        
    # Now one by one
    print 'Now one by one........................'
    cur.execute('select * from yves order by 1,2')
    while True:
        row = cur.fetchone()
        if row == None:
                break
        print row[0], '-', row[1]
    
except lite.Error, e:    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    if con:
        con.close()
