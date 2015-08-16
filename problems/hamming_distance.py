"""
Given two strings s and t of equal length,
the Hamming distance between s and t,
denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.
"""


def hd(s, t):
    if len(s) != len(t):
        raise ArithmeticError("sequences must have equal lengths")
    return sum([1 for x, y in zip(s, t) if x != y])


assert hd('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7
