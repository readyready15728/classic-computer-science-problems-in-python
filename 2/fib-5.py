def fib(n):
    if n == 0:
        return 0 # Special case

    last = 0
    next_val = 1 # Name chosen to avoid clobbering next()

    for _ in range(1, n):
        last, next_val = next_val, last + next_val

    return next_val

print(fib(50))
