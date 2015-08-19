"""
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""


def find_motif_locations(dna, motif):
    j = len(motif)
    return [str(i+1) for i in xrange(len(dna)-j+1) if dna[i:i+j] == motif]


def find_motif_locations_2(dna, motif):
    i = dna.find(motif)

    while i != -1:
        yield str(i+1)
        i = dna.find(motif, i+1)


assert find_motif_locations('GATATATGCATATACTT', 'ATAT') == ['2', '4', '10']
assert find_motif_locations('GATATATGCATATACTT', 'CTT') == ['15']


if __name__ == '__main__':
    with open("/Users/osharabi/Downloads/rosalind_subs.txt") as f:
        d, m = f.read().split()
    indices = find_motif_locations(d, m)
    print " ".join(indices)

    indices2 = (i for i in find_motif_locations_2(d, m))
    print " ".join(indices2)




