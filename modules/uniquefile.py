'''
function for making unique non-existent file name 
with saving source file extension
'''
import os
import sys

__author__ = 'Denis Barmenkov <denis.barmenkov@gmail.com>'
__source__ = 'http://code.activestate.com/recipes/577200-make-unique-file-name/'

def add_unique_postfix(fn):
    if not os.path.exists(fn):
        return fn

    path, name = os.path.split(fn)
    name, ext = os.path.splitext(name)

    make_fn = lambda i: os.path.join(path, '%s(%d)%s' % (name, i, ext))

    for i in xrange(2, sys.maxint):
        uni_fn = make_fn(i)
        if not os.path.exists(uni_fn):
            return uni_fn

    return None
