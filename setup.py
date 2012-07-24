from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(ext_modules = [
    Extension('something', ['something.py', 'something.pxd']),
    Extension('pyx_something', ['pyx_something.pyx']),
    ],
    cmdclass = {'build_ext':build_ext}
)
