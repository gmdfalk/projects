#!/usr/bin/env python2

#~ from __future__ import division, print_function
import urllib
from os.path import basename
from shutil import copyfileobj

url = "http://www.asdf.com/89asdf.gif"
#~ url = "http://download.thinkbroadband.com/5MB.zip"
origin = urllib.urlopen(url)
dest = basename(url)

def shcopy():
    with open(dest, 'wb') as f:
        copyfileobj(origin, f)

def urlretr():
    urllib.urlretrieve(url, basename(url))

def test(func, iterations=1):
    """Unique values, defeats memo-ization."""
    for x in range(iterations):
        func()

def timethese():
    import timeit
    
    setup = 'from __main__ import test, shcopy, urlretr'
    n = 50
    
    t1 = timeit.repeat('test(shcopy)', setup, number=n)
    t2 = timeit.repeat('test(urlretr)', setup, number=n)
    print 'shcopy', t1
    print 'urlretr', t2
    print 'Difference', min(t1) / min(t2)
    
if __name__ == "__main__":
    timethese()
