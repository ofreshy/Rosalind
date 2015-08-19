
from collections import defaultdict
import StringIO


from utils import fasta_reader

order = ("A", "C", "G", "T")


def solve(fd):
    def bin():
        return defaultdict(int)
    bins = defaultdict(bin)
    for _, seq in fasta_reader.fasta_concat_reader(fd):
        add_seq_to_bin(seq, bins)

    # now we got in bins the profile, get the consensus
    n = len(seq)
    consensus = get_consensus(bins, n)
    # print it nicely
    print "".join(consensus)
    for o in order:
        obin = bins[o]
        print "%s: %s" % (o, " ".join([str(obin[i+1]) for i in xrange(n)]))


def add_seq_to_bin(seq, bins):
    for i, s in enumerate(seq):
        bins[s][i+1] += 1


def get_consensus(bins, n):
    consensus = []
    for i in xrange(n):
        most_commons = max([(bins[l][i+1], l) for l in order])
        consensus.append(most_commons[1])
    return consensus


data = StringIO.StringIO("""
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
""")

sol = solve(data)


def main():
    with open("/Users/osharabi/Downloads/rosalind_cons.txt") as f:
        solve(f.read())

if __name__ == '__main__':
    # main()
    pass








