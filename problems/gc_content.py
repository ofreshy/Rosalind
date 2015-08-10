"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""


def calc_gc_score(data):
    nom, denom = 0.0, 0.0
    for line in data:
        clean_line = line.strip()
        for s in clean_line:
            if s in ("G", "C", "T", "A"):
                denom += 1
                if s in ("G", "C"):
                    nom += 1
    if not denom:
        return denom
    return nom / denom


def read_cg(lines):
    candidate = None, 0.0
    data = []
    for line in lines:
        if line.startswith(">"):
            gc_score = calc_gc_score(data)
            if gc_score > candidate[1]:
                candidate = header, gc_score
            data = []
            header = line
        else:
            data.append(line)
    if data:
        gc_score = calc_gc_score(data)
        if gc_score > candidate[1]:
            candidate = header, gc_score

    return "%s\n%.7f" % (candidate[0].strip().strip(">"), candidate[1] * 100)


import StringIO


ds = StringIO.StringIO("""

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")

assert read_cg(ds) == "Rosalind_0808\n60.9195402"