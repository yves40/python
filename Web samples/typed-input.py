#
#   Test a controlled input
#

import sys

#import cx_Oracle

#try:
#    con = cx_Oracle.connect('pythonhol/welcome@localhost/orcl')
#except:
#    print 'An error occured, unable to connect'

while True:
    try:
        sys.stdout.write('Your input please : ')
        line = sys.stdin.readline()
        x = int(line)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


print "That's it"
