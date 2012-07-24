#!/usr/bin/env python

import sys
import timeit

# Module to use and description to output
descr, modname = sys.argv[1:3]

# Timing parameters
N = 10000000
repeats = 3

# test value of output
result = __import__(modname).identity(N)

# Run timing tests and print output
stmt = 'import {0}; {0}.identity({1})'.format(modname, N)
t = timeit.timeit(stmt, number=repeats) * (1e9 / (repeats * N))
print descr, result, t, 'ns per loop iteration'
