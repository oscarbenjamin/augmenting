#!/usr/bin/env python

import timeit

import py_something, cy_something, cy_augmenting

stmts = [
    ('Pure python :', 'import py_something; py_something.identity({0})'),
    ('Pure cython :', 'import cy_something; cy_something.identity({0})'),
    ('Augmenting  :', 'import cy_augmenting; cy_augmenting.identity({0})'),
]

N = 10000000

for descr, stmt in stmts:
    print descr, timeit.timeit(stmt.format(N), number=3)