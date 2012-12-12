===========
Stats
===========

Stats provides tools which can be used for data collection and analysis.
Usage might look like this::

    #!/usr/bin/env python

    from stats import ReservoirSample

    print 'Building a sample of some larger data set'
    s = ReservoirSample(100)
    for value in some_really_large_list
        s.add(value)
    print 'Printing sample'
    for v in s:
        print v

