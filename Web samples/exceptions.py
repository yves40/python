#!/usr/bin/python

# Python exception handling.
# Find all exception codes here : http://www.tutorialspoint.com/python/python_exceptions.htm

'''
Exception           A base class for most error types
AttributeError      Raised by syntax obj.foo, if obj has no member named foo
EOFError            Raised if “end of file” reached for console or file input
IOError             Raised upon failure of I/O operation (e.g., opening file)
IndexError          Raised if index to sequence is out of bounds
KeyError            Raised if nonexistent key requested for set or dictionary
KeyboardInterrupt   Raised if user types ctrl-C while program is executing
NameError           Raised if nonexistent identifier used
StopIteration       Raised by next(iterator) if no element; see Section 1.8
TypeError           Raised when wrong type of parameter is sent to a function
ValueError          Raised when parameter has invalid value (e.g., sqrt(−5))
ZeroDivisionError   Raised when any division operator used with 0 as divisor
'''
import random
i = random.randrange(0, 8)
j = random.randrange(-1, 6)
print i, j

# Get a nice little array, then try a bunch of dangerous stuff.
some = [3, 10, 0, 8, 18];
try:
    # We try to execute this block.
    den = some[j] / i
    print "A:", den
    frac = (i + j) / den
    print "B:", frac
    if frac < 2:
        k = 3
    else:
        k = 'mike'
    print "C:", k
    print "D:", some[k]
# This is the catch block.
except ZeroDivisionError:
    print "\nDivision by zero."
except TypeError, detail:
    # The detail provides extra information about the exception.
    print "\nSome type mismatch:", detail
except IndexError, detail:
    print "\nSome value is out of range:", detail
except:
    # Except without an exception name catches any exception.
    print "\nSomething else went wrong."

# An else attached to an except block is run if no exception occurrs.
else:
    print "\nThat's odd, nothing went wrong."
    
