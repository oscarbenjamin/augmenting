from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(ext_modules = [Extension('cy_something', ['py_something.py'])],
      cmdclass = {'build_ext':build_ext})
