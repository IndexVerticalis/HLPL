import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"{func.__name__} - {end - start:.6f} сек")
        return result
    return wrapper

def next_fib(a, b):
    return a + b

@timeit
def fib_while(a, b, n):
    if n == 0:
        return []
    if n == 1:
        return [a]
    
    res = [a, b]
    while len(res) < n:
        a, b = b, next_fib(a, b)
        res.append(b)
    return res

@timeit
def fib_range(a, b, n):
    if n == 0:
        return []
    if n == 1:
        return [a]
    
    res = [a, b]
    for _ in range(n - 2):
        a, b = b, next_fib(a, b)
        res.append(b)
    return res

@timeit
def fib_generator(a, b, n):
    def gen():
        if n == 0:
            return
        x, y = a, b
        yield x
        for _ in range(n - 1):
            yield y
            x, y = y, next_fib(x, y)

    return list(gen())
