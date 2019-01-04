#!/usr/bin/python
#
# Python program to demonstrate for loops.
#

# The for loop goes through a list, like foreach in
# some other languages.  A useful construct.
for x in ['Bill', 'Alice', 'Joe', 'Sue' ]:
    print x, 'likes jelly beans.'

# The range operator simply creates a list of numbers
# in the indicated range.  Note that the range ends
# before the second argument.
print range(5, 10)

# Range works with for to create the traditional for loop.
for y in range(2, 10):
    print y,
print

for y in range(2, 10, 2):
    print y,
print

for y in range(20, 10, -1):
    print y,
print
##############################################################################
# A few more loops.

# Powers of 2 (for no obvious reason)
power = 1
for y in range(0,17):
    print "2 to the", y, "is", power
    power = 2 * power
    
# Scanning a list.
fred = ['And', 'now', 'for', 'something', 'completely', 'different.'];
for i in range(0,len(fred)):
    print i, fred[i]
