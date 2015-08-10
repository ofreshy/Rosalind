"""
FASTA format is as follow :

>Taxon1
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Taxon2
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Taxon3
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""


def fasta_simple_reader(fd):
    """
    Generates fasta data in tuple fomrat.

    Does not concat strings
    Removes white space
    :param fd: iterator over data lines
    :return: generator of header / data lines tuples
    """
    id_line = None
    data_lines = []
    for line in fd:
        if line.startswith(">"):
            if id_line:
                yield id_line, data_lines
            id_line = line.strip(">").strip()
            data_lines = []
        else:
            data_line = line.strip()
            if data_line:
                data_lines.append(data_line)
    yield id_line, data_lines


def concat_fasta(simple_reader):
    """
    concats the data lines from a simple fasta reader
    """
    for tup in simple_reader:
        yield tup[0], "".join(tup[1])


def fasta_concat_reader(fd):
    """
    Convenience function to return a concat string of fasta data
    """
    return concat_fasta(fasta_simple_reader(fd))
