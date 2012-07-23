#!/bin/bash

set -o errexit

python setup.py build_ext --inplace "$@"

echo
echo
echo Python
time python -c 'import py_something; print py_something.identity(10000000),'

echo
echo
echo Cython .pyx
time python -c 'import cy_something; print cy_something.identity(10000000),'

echo
echo
echo Cython augmenting .pxd
time python -c 'import cy_augmenting; print cy_augmenting.identity(10000000),'
