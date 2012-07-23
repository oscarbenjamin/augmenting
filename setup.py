from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(ext_modules = [
    Extension('cy_augmenting', ['py_something.py', 'py_something.pxd']),
    Extension('cy_something', ['cy_something.pyx']),
    ],
    cmdclass = {'build_ext':build_ext}
)

import py_something
import cy_augmenting
import cy_something
