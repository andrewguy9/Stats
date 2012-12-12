#!/usr/bin/env python

from stats.sample import ReservoirSample

N = 3
n = 15

s = ReservoirSample(N)
for i in range(n):
  s.add(i)
for i in s:
  assert(i >=0 and i <n)

assert(N == s.sample_size() )
assert(n == s.num_added() )
assert(N == len(s.data) )

N = 5
n = 5
s = ReservoirSample(N)
for i in range(n):
  s.add(i)

