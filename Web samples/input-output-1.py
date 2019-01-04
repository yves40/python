#!/usr/bin/python

# Script to copy standard input to standard output, one line at a time.

# This gets various items to interfaces with the OS, including the
# standard input stream.
import sys

# Readline is a method of stdin, which is in the standard object sys.
# It returns the empty string on EOF.

#line = sys.stdin.readline()

# The string line works as the while test.  As several other scripting
# languages, the empty string is treated as false, other strings are treated
# as true.
# Loop until terminated by the break statement.

while 1:
    # Get the line, exit if none.
    sys.stdout.write('Your input please : ')
    line = sys.stdin.readline()

    if ( len(line)==1):     # CR only
        break
    if not line:
        break
    if ( line[:-1] == "exit"):
        break
    else: 
        # Print the line read.
        print line[:-1]

print "Goodbye"

