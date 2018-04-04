def fib(n):
    """
    O(n) - Linear runtime
    """
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]

def fib_recursive(n):
    """
    O(2^n) - Exponential (bad!!)
    IMPROVE WITH MEMOIZATION
    """
    if n < 2:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_recursive_(n):
    if n < 2:
        return n
    return fib_memoization(n-1) + fib_memoization(n-2)

cache = {}    
def fib_memoization(n):
    """
    O(n)
    """
    if n not in cache.keys():
        cache[n] = fib_recursive_(n)
    return cache[n]