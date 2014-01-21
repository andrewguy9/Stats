#!/usr/bin/env python

import math

class Cumlative:
    def __init__(self):
        self.total = 0

    def __call__(self, value=None):
        if value is not None:
            self.total+=value
        return self.total

class CumlativeMovingAverage:
  def __init__(self):
    self.n = Cumlative()
    self.total = Cumlative()

  def __call__(self, value=None):
      return self.total(value) / self.n(1)

# Exponentially moving average: Returns a moving average where a given data point has
# less and less impact on the current value as new points come in.
# alpha is the proportion of the measurement which should be determined
# by this datapoint.
# S(1) = Y(1)
# S(t) = alpha * Y(t) + (1 - alpha) * S(t-1)
# where alpha is between 0 and 1
class ExponentialMovingAverage:
  def __init__(self, initial):
    self.s = float(initial)
 
  def __call__(self, y = None, alpha = None):
    assert((y is None) == (alpha is None))
    if y is not None:
      self.s = alpha * y + (1-alpha)*self.s
    return self.s

# S(n) = a*Y(n) + (1-a)*S(n-1)
# Where a is function of time between n and n-1.
# a( t(n) - t(n-1) ) = 1 - exp(-(t(n) - t(n-1))/(W*60))
# Where time is in seconds and W is the period of time in minutes over which the
# average is said to be over.
class MovingAverage:
  def __init__(self, period, init_value, init_time):
    self.w = float(period)
    self.t_last = float(init_time)
    self.avg = ExponentialMovingAverage(init_value)

  def __call__(self, value=None, t=None):
    assert((value is None) == (t is None))
    if value is not None:
      delta_t = t - self.t_last
      self.t_last = t
      alpha = 1-math.exp(-delta_t/self.w)
    else:
      alpha = None
    return self.avg(value, alpha)

class MovingRate:
  def __init__(self, period, t):
    self.w = float(period)
    self.t_last = float(t)
    self.rate = float(0)

  def __call__(self, count=None, t=None):
    assert((count is None) == (t is None))
    if count is not None:
      delta = t - self.t_last
      self.t_last = t
      alpha = math.exp(-delta/self.w)
      self.rate = count + self.rate*alpha
    return self.rate

