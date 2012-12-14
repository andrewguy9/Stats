#!/usr/bin/env python

import random
import unittest
from stats.percentile import percentiles

class TestPercentiles(unittest.TestCase):

  def setUp(self):
    self.seq = range(37)

  def testZero(self):
    self.assertEqual(percentiles(self.seq,[0.0]), [0])

  def testOne(self):
    self.assertEqual(percentiles(self.seq,[1.0]), [36])

  def testHalf(self):
    self.assertEqual(percentiles(self.seq,[0.5]), [18])

if __name__ == '__main__':
  unittest.main()

