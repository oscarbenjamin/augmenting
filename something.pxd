import cython

@cython.locals(n = cython.int, total = cython.int)
cpdef int identity(int N)
