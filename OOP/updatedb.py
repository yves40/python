#-----------------------------------------------------------------------------------------------------------
#   updatedb.py
#
#   Aug 07 2016     Initial
#-----------------------------------------------------------------------------------------------------------

from collections import namedtuple
import shelve

# Named Tupple to store constants
ProgramInfo=namedtuple('Z', ['Name','Version','Author'])     # Make a generated class
proginfo=ProgramInfo('updatedb.py ', '1.00, Aug 07 2016  ', 'Y.T')
#
#
#
print "Another scan of the shelve store, sorted"
db = shelve.open('persondb.data') # Filename where objects are stored
print "Here are the sorted keys : "
for key in sorted(db):
        print "Key : ", key

# Now displaying more details
print "\nSome details now\n"
for key in sorted(db):
        reader = db[key]
        print (' %20s --- %.2f ' % (reader.lastName(), reader.pay))

# Give a raise to everyone
for key in sorted(db):
        reader = db[key]
        reader.giveRaise(.10)
        db[key] = reader

print "\nAfter the raise\n"
for key in sorted(db):
        reader = db[key]
        print (' %20s --- %0.2f ' % (reader.lastName(), reader.pay))

print "\nClose the store"
db.close()

