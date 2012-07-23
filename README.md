augmenting
==========

Test for augmenting pxd files

This project is just for me to test how to use cython to generate an extension
from a pure python module with the use of an augmenting pxd file as described
here:
http://docs.cython.org/src/tutorial/pure.html#augmenting-pxd

I would like to be able to do this as it seems like a good way to maintain a
pure python module along with a cython accelerated version.

how to use
----------

Download and run::

    $ python setup.py build_ext --inplace
    $ python test.py

The output I get::

    $ python test.py
    Timings for the different implementations:
    Pure python : 243.88935674 ns per loop iteration
    Pure cython : 1.29719247757 ns per loop iteration
    Augmenting  : 199.397050087 ns per loop iteration
