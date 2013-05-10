#!/usr/bin/env python

from time import time

def periodic(timeout):
    def decorator(f):
        def injection(*args, **kwargs):
            now = time()
            if now > injection.last_time + timeout:
                print "Running f"
                injection.last_time = now
                return f(*args, **kwargs)
            else:
                print "skipping f"
        injection.last_time = 0
        return injection
    return decorator

