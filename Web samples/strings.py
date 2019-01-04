# Some tests on strings

#!/usr/bin/python

# Strings in single quotes.
s1 = 'I\'m single'

# Double quotes are the same.  You just have to end with the same character
# you started with, and you don't have to escape the other one.
s2 = "I'm double double"

# You can create multi-line strings with triple quotes (triple double quotes
# work, too.)  The newlines stay in the string.
s3 = '''I'm very long-winded and I really need
to take up more than one line.  That way I can say all the very
`important' things which I must tell you.  Strings like me are useful
when you must print a long set of instructions, etc.'''

# String literals may be concatinated by a space.
s4 = 'left' "right" 'left'

# Any string expression may be concatinated by a + (Java style).
s5 = s1 + "\n" + s2

print s5 + '\n' + s3, "\n", s4

print 's5 has', len(s5), 'characters'

#
#
#


# Strings have various escapes.
print "******************************************************************"
print "Hi\nth\ere,\thow \141\x72\145\x20you?"

# Raw strings ignore them.
print r"Hi\nth\ere,\thow \141\x72\145\x20you?"

print

# Very useful when building file paths on Windows.  
badpath = 'C:\that\new\stuff.txt';
print badpath
path = r'C:\that\new\stuff.txt';
print path



# Use brackets for string subscripting and substrings.
print "******************************************************************"
bozon = 'Cheer for Friday'
#        0123456789012345

# Index at zero.
print bozon[0], bozon[1], bozon[15]

# You may not use [] on the left of an assignment, however.

# Use the colon to describe ranges.  The last character is not part of the
# range.
print bozon[0:5] + ", " + bozon[0:6] + bozon[10:16] + '!'

# Defaults to first and last.
print bozon[:5] + ", " + bozon[:6] + bozon[10:] + '!'

# The * operator repeats strings (like x in perl).
print bozon[:6] * 3 + '!'

# Negatives index back from the right, the rightmost character being -1.
print bozon[-1] + ' ' + bozon[-10:-6]

