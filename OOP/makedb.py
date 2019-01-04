#-----------------------------------------------------------------------------------------------------------
#   makedb.py
#
#   Aug 06 2016     Initial
#   Aug 07 2016     Follow up, reading the book
#-----------------------------------------------------------------------------------------------------------

from Person import Person
from Manager import Manager
from collections import namedtuple
import shelve
import sys

# Named Tupple to store constants
ProgramInfo=namedtuple('Z', ['Name','Version','Author'])     # Make a generated class
proginfo=ProgramInfo('makedb.py ', '1.02, Aug 06 2016  ', 'Y.T')

# Create a few persons
bob = Person('Bob Smith', pay=100000) # Test the class
sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
nini = Person('Barbul', 'Student', 12000)
dad = Person("Dad")
yves = Manager('Yves', 180000)

defaultname = 'persondb.data'

print sys.argv

if len(sys.argv) > 1 :
    defaultname = sys.argv[1]
    print 'Output file name forced to : ', defaultname

print "Open the shelve store"
db = shelve.open(defaultname) # Filename where objects are stored

for obj in (bob, sue, nini, dad, yves): # Use object's name attr as key
    db[obj.name] = obj # Store object on shelve by key. Here the key is just the object name

print "Close the store"
db.close()

print "Re-Open the shelve store"
db = shelve.open('persondb.data') # Filename where objects are stored
print "The DB file has now ", len(db), " entries"
print "Here are the keys : "
keylist = list(db.keys())
for key in keylist:
        print "Key : ", key

print "Close the store"
db.close()
