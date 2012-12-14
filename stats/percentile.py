#!/usr/bin/python

from math import floor

# Takes in a list of values which are in some sorted order.
# Returns the values at various percentils.
def percentiles(values, percentiles):
  assert(all(map(lambda x:x<=1.0, percentiles)))
  results = []
  l = list(values)
  for p in percentiles:
    index = int(floor(p * (len(l)-1)))
    results.append(l[index])
  return results

