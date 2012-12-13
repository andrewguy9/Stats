#!/usr/bin/env python

import unittest
import random
import math
import stats.counter as counter

class TestCounters(unittest.TestCase):
  def setUp(self):
    rnd = []
    seq = range(25000)
    for t in seq:
      rnd.append(random.randint(0,1))
    self.data = zip(seq, rnd)

  def testCumlativeMovingAverage(self):
    tot = counter.CumlativeMovingAverage()
    for t,v in self.data:
      tot.update(v)
    self.assertTrue(abs(tot.get()-.5)<.02)

  def testExponentialMovingAverage(self):
    avg = counter.ExponentialMovingAverage()
    for t,v in self.data:
      avg.update(v, 1.0/5000.0)
    self.assertTrue(abs(avg.get()-.5)<.02)

  def testMovingAverage(self):
    t = 0
    aot = counter.MovingAverage(5000.0,lambda: t)
    for t,v in self.data:
      aot.update(v)
    self.assertTrue(abs(aot.get()-.5)<.02)

  def testMovingRate(self):
    t = 0
    rat = counter.MovingRate(5000.0, lambda: t)
    for t,v in self.data:
      rat.update(v)
    self.assertTrue(abs(rat.get()/5000-.5)<.02)

if __name__ == '__main__':
  unittest.main()
