def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

print(fib(5))
print(fib(10))
print(fib(20))
# print(fib(50))
