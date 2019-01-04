#!/usr/bin/python

# Python list.
# Some tests
#



fred = [ 'The', 'answer', 'to', 'your', 'question', 'is', 24 ]
print 'A:', fred

# Subscript, as strings.  Returns an item from the list.
print 'B:', fred[0], fred[2], fred[6], fred[-1], fred[-4]

# Ranges create a "slice" -- a sublist.
print 'C:', fred[2:5], fred[-6:-3], fred[4:5], fred[3:3]

# Individual items may be replaced.
fred[1] = 'response'
fred[-1] = fred[-1] + 200
fred[-3] = 'query'
print 'D:', fred

# Assignment to slices is allowed, and can change the list size.
fred[0:2] = [ 'An', 'unlikely', 'answer' ]
fred[-1:-1] = [ 'a', 'conservative' ]
print 'E:', fred

# Sublists are allowed.
mike = [ 3, 4, ['and', 'also', 'a'], 52]
print 'F:', mike
mike[0] = [2, '+', 1]
mike[2] = 11
print 'G:', mike

fred[1:3] = [fred[1:3]]
fred[-1:] = [mike]
print 'H:', fred

print 'Fred has', len(fred), 'entries.'
##############################################################################
# Several other operations on lists.

fred = [ 'Alice', 'goes', 'to', 'market' ]
print 'A:', fred

fred.extend([ 'with', 'Mike' ])
print 'B:', fred

last = fred.pop()
fred.append('Fred')

print 'C:', fred

print 'So much for Mike.'
print 'There are', len(fred), 'items in fred.'
print 'The word market is located at position', fred.index('market')

fred = [ 'On', 'Tuesday,' ] + fred
print 'D:', fred

fred.reverse()
print 'E:', fred

fred.sort()
print 'F:', fred
