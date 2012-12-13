#!/usr/bin/python

def maxima(iterator):
  b = iterator.next()
  c = iterator.next()
  for n in iterator:
    if c != n:
      a = b
      b = c
      c = n
      if (a < b and b > c):
        yield b

def minima(iterator):
  b = iterator.next()
  c = iterator.next()
  for n in iterator:
    if c != n:
      a = b
      b = c
      c = n
      if (a > b and b < c):
        yield b

