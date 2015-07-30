
"""
Fib
"""


def fib(n, k):
    if n < 2:
        return 1

    def next_generation():
        return n2 + k * n1

    n2 = 1
    n1 = 1
    for i in range(n-2):
        n_gen = next_generation()
        n2, n1 = n_gen, n2
    return n_gen


assert fib(5, 3) == 19
print fib(28 , 3)

