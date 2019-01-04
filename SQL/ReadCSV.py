#!/usr/bin/python
# coding: utf8
#-----------------------------------------------------------------------------------------------------------
#   ReadCSV.py
#
#   Aug 09 2016     Initial
#-----------------------------------------------------------------------------------------------------------import sys
from __future__ import unicode_literals
#
#   Look @ Windows command : chcp
#

import logging
import sys, string
import encodings
import sqlite3 as lite

#import codecs

#   Configure a logger
logging.basicConfig(level=logging.INFO)
# create a file handler
handler = logging.FileHandler('mylogger.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Get a logger
log = logging.getLogger(__name__)
# add the file handler to the logger
log.addHandler(handler)

print
log.info('Starting')


con = lite.connect('../testdb')
cur = con.cursor()

log.info('Begin transaction')
cur.execute("""begin transaction""")


print ''.join('- ' + e + '\n' for e in sorted(set(encodings.aliases.aliases.values())))
log.info('Entering the file loop')
print

for fn in sys.argv[1:]:
    try:
#       fin = codecs.open(fn, 'r', 'utf-8')
        fin = open(fn, 'r')
    except:
        (type, detail) = sys.exc_info()[:2]
        print "\n*** %s: %s: %s ***" % (fn, type, detail)
        continue
    print "\n*** Contents of", fn, "***\n\n"
    
    # Print the file, with line numbers.
    lno = 1
    line = u''
    while lno < 10:
        line = fin.readline()
        if not line: 
                break;
#        line.encode('utf-8')
        print '%5d: %-s' % (lno, line[:-1])
        fields = string.split(line, ',')
        region = fields[2]
        department = fields[5]
        commune = fields[8]
        codepostal = fields[9]
        latitude = fields[11]
        longitude = fields[12]
        print '\t', region, '-', department, '-', commune, '-', codepostal, '-', latitude , '-', longitude
        lno = lno + 1

        cur.execute("""INSERT INTO communes (nomregion, departement, commune, codepostal, latitude, longitude) VALUES (?,?,?,?,?,?)""", 
                  (region, department, commune, codepostal, latitude, longitude))

    fin.close()

print
log.info('Commit')
cur.execute("""Commit""")
con.close()
print
log.info('Exit')

print