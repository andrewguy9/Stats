#!/usr/bin/env python

import unittest
from stats.extrema import maxima as maxima
from stats.extrema import minima as minima

class TestExtrema(unittest.TestCase):
  def testBasic(self):
    self.assertEqual(list(maxima(iter([1,2,3,2,1]))), [3])
    self.assertEqual(list(minima(iter([3,2,1,2,3]))), [1])

  def testTwo(self):
    self.assertEqual(list(maxima(iter([1,2,3,2,3,4,3,2,1]))), [3,4])
    self.assertEqual(list(minima(iter([3,2,1,2,3,4,3,2,3]))), [1,2])

  def testRepeat(self):
    self.assertEqual(list(maxima(iter([1,1,2,2,3,3,2,2,1,1]))), [3])
    self.assertEqual(list(minima(iter([3,3,2,2,1,1,2,2,3,3]))), [1])

  def testPlateau(self):
    self.assertEqual(list(maxima(iter([1,2,3,3,2,1]))), [3])
    self.assertEqual(list(minima(iter([3,2,1,1,2,3]))), [1])

  def testFlat(self):
    self.assertEqual(list(maxima(iter([1,1,1]))), [])
    self.assertEqual(list(minima(iter([1,1,1]))), [])

  def testAscending(self):
    self.assertEqual(list(maxima(iter([1,2,3]))), [])
    self.assertEqual(list(minima(iter([1,2,3]))), [])

  def testDecending(self):
    self.assertEqual(list(maxima(iter([3,2,1]))), [])
    self.assertEqual(list(minima(iter([3,2,1]))), [])

if __name__ == '__main__':
  unittest.main()
