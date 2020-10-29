class Fib:
    memo = {0: 0, 1: 1}

    @staticmethod
    def fib(n):
        if n not in Fib.memo:
            Fib.memo[n] = Fib.fib(n - 2) + Fib.fib(n - 1)
        return Fib.memo[n]

print(Fib.fib(50))
