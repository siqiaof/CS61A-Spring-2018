def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)


def count_k(n, k):
    if n == 0:
        return 1
    else:
        if n >= k:
            return add_k(count_k, n, k)
        else:
            return count_k(n, k-1)

def add_k(f, n, k):
    i = 1
    a = 0
    while i <= k:
        a += f(n-i, k)
        i += 1
    return a
        
