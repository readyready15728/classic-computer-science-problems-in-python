def fib(n):
    yield 0 # Special case
    if n > 0:
        yield 1 # Special case

    last = 0
    next_val = 1 # Name chosen to avoid clobbering next()

    for _ in range(1, n):
        last, next_val = next_val, last + next_val
        yield next_val

for i in fib(50):
    print(i)
