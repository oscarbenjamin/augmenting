
cpdef int identity(int N):
    cdef int n, total
    for n in range(N):
        total += 1
    return total
