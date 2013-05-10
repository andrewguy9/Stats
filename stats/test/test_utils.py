#!/usr/bin/env python

import unittest
from stats.utils import periodic
from time import sleep

@periodic(5)
def func1(p1,p2):
    print "\tfunction 1: %s %s" % (p1,p2)

@periodic(.1)
def func2(foo='bar', tar='car'):
    print "\tfunctino 2: %s %s" % (foo, tar)

class TestUtils(unittest.TestCase):
    def testFunc1(self):
        print ""
        print "Testing function 1: do,skip X 3"
        sleep(5)
        func1(1,2)
        func1(1,2)
        func1(1,2)
        func1(1,2)
    def testFunc2(self):
        print ""
        print "Testing function 2: do X 4"
        sleep(5)
        func2()
        sleep(.2)
        func2()
        sleep(.2)
        func2()
        sleep(.2)
        func2()
    def testFunc3(self):
        print ""
        print "Testing both: hit, hit, (miss, hit) X 4"
        sleep(5)
        func1(1,2)
        func2()
        sleep(.2)
        func1(1,2)
        func2()
        sleep(.2)
        func1(1,2)
        func2()
        sleep(.2)
        func1(1,2)
        func2()

