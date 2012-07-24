
cpdef int identity(int N):
    cdef int total, n
    total = 0
    for n in range(N):
        total += 1
    return total
