#!/usr/bin/env python

import unittest
from stats.sample import ReservoirSample

class TestSample(unittest.TestCase):

  def testsample(self):
    N = 3
    n = 15

    s = ReservoirSample(N)
    for i in range(n):
      s.add(i)
    for i in s:
      self.assertTrue(i >=0 and i <n)

    self.assertTrue(N == s.sample_size() )
    self.assertTrue(n == s.num_added() )
    self.assertTrue(N == len(s.data) )

    N = 5
    n = 5
    s = ReservoirSample(N)
    for i in range(n):
      s.add(i)

if __name__ == '__main__':
  unittest.main()
