#!/usr/bin/python

# The os.path module has operations for manipulating file name paths
# for whaterver system you're running on.

import os.path as osp
import os as os
import time
import sys
import timeit as tim


from os.path import *

if len(sys.argv) > 1:
    filelist = sys.argv[1:]
else: # Build a dummy list
    filelist = [ '.', 'c:\\tools', '1.py', '..', 'bogus', 'ospathfacility.py' ]    

for fn in filelist:
    print '%-15s' % fn + ':',

    # Don't forget: These operations are os.path.whatever.

    # Is it there?
    if exists(fn):
        print 'exists,',
    else:
        print 'nonexistent'
        print
        continue

    # Absolute path?
    if isabs(fn):
        print 'absolute,',
        print 'directory', dirname(fn)+',', 'base', basename(fn)+','
        print ' ' * 16,
    else:
        print 'relative,',

    # What sort of thing is it?
    if isfile(fn): print 'plain file,',
    elif isdir(fn): print 'directory,',
    else: print 'strange,',

    # Extension.
    print 'extension', splitext(fn)[1]+',',

    # Size
    print getsize(fn), 'bytes.'

    print


for fn in filelist:
    if osp.exists(fn) :
        print 'Checked with my osp import : [', fn, "] last modified on " , time.ctime(os.path.getmtime(fn)),
        print " created on ", time.ctime(os.path.getctime(fn))
    else:
        print "Houston, got a problem here!!!! [", fn, "] is not on this system"

