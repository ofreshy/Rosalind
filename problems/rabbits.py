
"""
Immortal Rabbits,
Fibbonachi Series with k pairs on each second month
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


"""
Mortal Rabbits
"""


def mortal(n, m):
    if m == 1:
        return 0
    if m == 2:
        return 1
    if n < 3:
        return 1

    # month in life is key, value is number of pairs

    def next_generation(cur_generation):
        new_gen = {}
        new_borns = 0
        for months, pairs in cur_generation.items():
            # month == 1 are too young to reproduce
            if months != 1:
                new_borns += pairs
            # months == m are dead after reproducing so we do not add them
            if months < m:
                new_gen[months+1] = pairs
        new_gen[1] = new_borns
        return new_gen

    generations = {2: 1}
    for i in range(2, n):
        generations = next_generation(generations)

    return sum([v for v in generations.values()])


print mortal(93, 4)


def fib_mortal(n, m):
    ages = [1] + [0]*(m-1)
    for i in xrange(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


print fib_mortal(93, 4)

