
def read_codon(condon_file_path):
    codon = {}
    with open(condon_file_path) as f:
        for line in f:
            if line:
                print line
                k, v = line.strip().replace('\n', '').split(' ')
                codon[k] = v
    return codon


CODON = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'ACU': 'T', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': 'Stop', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'UGA': 'Stop', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGA': 'R', 'GCU': 'A', 'UAG': 'Stop', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}


def rna_reader(seq):
    buf = []
    for s in seq:
        buf.append(s)
        if len(buf) == 3:
            yield "".join(buf)
            buf = []


def rna_to_protein(rna_seq):
    proteins = []
    for code in rna_reader(rna_seq):
        p = CODON.get(code)
        if p != 'Stop':
            proteins.append(p)
    return "".join(proteins)


assert rna_to_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'

rna_seq = 'AUGGAGCCUGGGUUGCUUUGGUACAAGUCCCAGUUCCCGUGGUCGAACAGAGAUAAUCAGCUUUGUGUCCGCCGGAAGAAUAUCCGCUCACCGCGGAGAAUGCGACGCGUUUUAUGGCCCCAGUUCCCUGAGCGAUAUAAGCAGCUUACCACAUCACCCUUGUGCGCUACUGAUUCCUGCCCUCCAUCUUAUUGCCAUAUGAAACCAACGUUAAUCGCGUCAAAAUUACAAUGCGGCCCCCUGUUCAAAUGGCCUUGGCCAACGAUCCUGGUCUCUAGCAGAGCUUGGGUGAUUUCUGGUGGUCGAGAGCAAGGGCGAGUGCUACCCGUUAAGCGAUCACUCCGGCUAACAUGCUCACGAAACAAAAUAAAGUGUACCGUCCUAGACUCCUCGGUGGUUGUUCUCGCUCUGGGAGACGAGACUCAUACGGACUUUCUCUUAGGACCUGGUCUUUGCGUCAUCACAGGCGUGGACAACAGCGAGCCGCCGAUAGUGGCAUAUGGGAGGGGAUACACCUUAUGUAAGCAGUGCAUGACAUCUAUUCCAUUCAGAGACGUAGGGGUUUUGAUGCCUUAUCAUUGGCUGACUAUGGGGAUCUGCAGCCUGAACACUAUCGUGGUCUAUCGCUUCUCCCGCGCCCCCUAUCCUGGUAGGGGUGGCCGAGGUCUAACGGUUAUCUCUGCGAUGCGCUGCUGGUUGGAGGCUGAUAUAUUCGUCUUCCUAUCUUCGCCCUUGACGCAUGGGGACGCAGGGGAUUUACAAAUGAUAGUCCGGAGACCUAACUGGAGGGUGUUGCAUGGCGAUUUCCUUUUGCUUCGUCUACUGUGGUACCGUGCUGACGCACGCAUAGAGGCCCGCGCCGUGCAGCAGCAGCCCCCGGUGUGUCGUGUAUCAGGCAACUCAAUAGCUCCGCCGCCCCCUGCAGAAUCAAUUUCUGACAUUUCUCACCUCGACCGCACGGGAUGUGGUCCCCGAUUCCGAUUGGGCUGGGGUCUAUCCGUAAACAUUUCUUACUCUGCACUCUACCGAUCCGAGCAACAGGUCCUAAAGGUCGAUGAUCAAAUGCGUCGCGGGGCAUGCUCUCGUGUACUCUUGCCUCUUUUUCCGUGCGUACCUCCUAGCGGCGUAAGUUUGCUUGGUAUGAAUAUGUCGUGUAGAGACAUCGACGCCGCUCUUAAUGCAACCGCUCCUGAAUCAAGCUUAAGCGAAUCCGACACACCUGGGCAGCCUAAAGUGCUGCACAUUUUAUCAAAAACUCCGACCCUCGGCGCGACGAAUGGUUGGGGUCAGGUAACACUACCCCCGUACUUCAAUCGUAAAGCGCCACUCCCUUGCUGUCCUUCGCAGCAUUCGCAGUCCUCCGAAUGGUCUAAUUACGCUCCAAAAGGACGUCCCUUUGCCAUUUGCGGUUGGGGCUUUAGCCUACUAGCAGCCGACAGCGUCACCCACCGGGCGGUGGCCCAGCGUGAUAGACCUCGAUCCAUAUUCCGGUUCCUGUCGGGUGCUCAGAGGCCCAACACCAGUUGCUCGAGCUAUGAUGAUAGCUCUAAUAUGCGCGCGAUUCCAGACAGUAAUCUCAUUAUUGUUUUGAUUGUCGCAUUUAUUUACAGUAAGCAAGGGUUGGUGCUCCGCCCUUCGGCGCCGCAUCCUUUCCUAUCGGGAUAUUGUACAACCCUUACACGUAUAUUCUUAGAAUUUGGUAGCCAUAAGUACACAACUGCAGAGAGACAACCUUUUACGGAAUACGAUAGGAACGACGCGGUUGAUCGUCACGUAGUGGUGGUGAAAAAACUGCCAGACGGUUGUCUUUCCUAUUAUCACGGUGGAGUUAGGCUGGUGCUGCUGCCGGGGCAAACUACCUGCAUGCUAGAAAGCCAGCAGAUUUUGUCUCUGGGGUCUAAAAUCCGGUGGUUGCUCGUGACGCAUGUUCUGAUAACAUACUUUACGCUUGUCAAGAUAACAUCGCUCUGUGUUCUUUCGUCCUUCGCCCUGUAUUACUGUGCUUGUAGCCGUCUAAGCGUUCAACUGUACAGAGAGAGUAUGAUUCGUAAAGUUCGCAAUUUAUCGUGUUUAACAACCCCAAUGUACAUCGGUAGAGGUCUACGGUCCACCGUGGGCAUCGGACUUUGUGGACCCGGAUUUCGAGCUUUUCUCGGAAGCCGGAUUCUGGGUCUACGACACCAAUUACACCAGAUGACUACCCUAUUAGCGAUAAUGCCAGCUAGAGCCACCACAGGGUGCCUAUACAGGAAAGAAAUGCGCGGUGCGGCUAAAAUGUGCGUGAAGAAGUCUGAGCGUUGGGGAAACGACCUGAAAGCUCUUGUAAUUCAACCACAGGACAGGAGUCAACCUGGGCUUGGCGGUCGCAAGGACCAUGCUCCAUACCUACCUUCAUGCAGAAAGCACUGCGUUUGUACGGACUUAAGCACAGUCAAGGGGCUUAGCGUACGCGACAUGACUUCUAGGACGAGGACUACUGCCUGCAGCAACGCUAAGUCCCCUGCUUUCCCUUGGAGUGGCACCUCCGAAUUACCCCUGAUUCGGUUCUUGCUGUCCGUUGCCUUCUCUUCCGAUCUGGUGAUGGAAUCUCGCUUUUUCAAAAUUCUAUGUUCGUGCUCAGGUAAUUUCGGCACUUCUUCCACGAGACCCAGAAUUAAGAUGUGCUUCUUCGAUGUAUAUAAUACUAGAUCAAGAGUUUUACCACAUCCAACCGUGAACCGGGGCACGACGAUUUCCGUAUUUAAGAUAUGUCUAAUGGACACAUUUUUCAUUGACAAGUCCCUUUCGAGCGGUCACCGGUGCAGGUACAGCGUUCCUCUCGCUAUGAGAGUCAAAAUCAGACAAAAGGCAAGCGCUGUGCGUCGACGAAGCUGGUAUGUGGGGAGAGUUGUCAACUCACGCAUCGGUGUAAUCGCCCUGACUGCCCUGUCGUUUGCUGGUAUACUCGAUGUAGUUCGAAAAACCCUCCCACGUUCCACCGAUUUGAAGGAUCAUUAUGCUGUGGGACGGUGCGAGCCCGCGUACCCGCGUCACGGGGAAUGGAUCACCAAGGGUUAUAAGCAUGUGCGCACAUCCGGGUCCAAGUCGGAGCUUUGGGAAGGUGGCAACCUCGACUGCUCAGGCAAUGCGAUUUCAACUUUGAAAGUCCCCAGUGUAGUAAGAACCGGCCGCUUGUUCAAAAUUUCACUCAUUACAACUGUGAAGGUUAAUGCGAUAGUGGAGCUCCAUCCGGCUGGAGUAACGACAAGGACCCAAGGACCGUGGGUAGUCGCAAGGCCAGAACGGGUUCGACAUGUGAUGGUUACACAUUACUUUAUGUCGGAUAACAGGCUUCUACAACUACACAAUCUAAUGCACAAUUAUGACCUGAAAGUUGGUUCCUCGGGGGAUAUCGAAGCCCCGCCCCUUCGGAAGGGUAGCAGUAUAGUGGAGUUAGUAAAAGCCGUAUCUGGUCUUAUGAGCACCUUGACAGCACUGAUCUUAGGAUAUCGAAGCGUAGGGAGCUCCUCGGAUAUUUCAUCGCGGCUUCUAGCUGCGAUCGACGCCACAAAACGAUGUGUGACAAAUUUUUCAGUCCUCAACGGUGAAGCUCAACAUUCGUGUACGCAAAGGGCACAGAGGAUUGAUUCCUGGGACCGCUGCCUUUGCGCAAAAACGCAUAAUCGUCUAGAAUUUGACGGAGCCGCAUGUAUCCCCAGUCCUCUACGAUCGGACCCUUGUAUAGACGGGUUUCCCCUACAUAGCAGCGAGCCUGCCAACUGUGUGUUCUUAACUCCCAAUUCAUCAAGGCUUUCCCCCGGUGUGAUGAAAUAUAAAACACGUAGCAACUACGGAUGUGUGUGCCAGAUUGGUCAAAUAGGCGGCUUUUGUCUAAUUCGUACAAUGUCUCUCUCGGAACACGGGUCUUGCCCCCGAGAUCUUUGUCCGACCCCGACGCCACGGUGGAGGUCAUGCUUGUCGUAUGGAUCCCUUAAUUCGGUAGGAUUCCAUUGUCCAGAGUCCCAUCUUUUGCCAAGUUACAGUAACGCCUGCCAGGAAAGGAUAGUCCGGCAUCAGAAGGCCUCUAUGAGGAGAGGCUCAAGUAUUUUCUCAGCAAUGAACCAGCGAUUUCUCCAGGCAGUGCCGGAGCCCAGGGGAUUCAUGGCGCAACUGAAGUCGUCUUCAACCGAGCACGAAAGUCACCCAGCCUGGGAUAAGCACACAUAUCAGUUAGACAGAGUCAAAGCUAAACAUACGCACAUGUUGAGGUUAAAAUCCGUCUUUAUCUGCUUACCAGUGGUCCCUGAUGUGUGCAAUCCAAAAUCGGGCAGCGCCUGGUGUAAUAUACACGCGCAGCGUUCCGGAUAUCCGGACCAAUGGACGAGGGUAAAUUUGCAGACUGUCCAAACAGAAGAGAUCACAGCUAUAAAGAUCUACUCGGUUAGCUGGCGCAACCUCUUCUCAGUACGUUGCCGCGCAAAAAGAGCGCCGGCACUACUAGCACUAGGCGCGUACCCCAUCCCUAUGCUAUCUGUACCGCUUGGCGACAUCCAUUCAACAACGACACCCGGUCCGACGAUGGUGCGAACUAGUUCGUCCCAGCAUUGUUUGACGGAGAGGGGAAAUCCAAUGCGUAGUCAUCACCUGCAAAAACCGAGCCAGACCAAUAACCAAGUGUGCCACCUUGUCUGGGGUGCUGCGUACAAGGCGGGCAUCGACGACGAAUACACAUUCUCCACUCUGCGUGGUAGAGCGGGUGGGGGAUCUCCCUCUAGGGCGAUGUGCUUGGCAGGUUCCGUACGUCUGCGACCCCGCUAUGUAACUAGACUGGGCCAGUCUUUAGCAAAUCCCGACCUCACUUUCGGGUCUAAUGUGUCUCCAAGAGUACAAAAUUCUGUUUGCGCCUGCUGCCUGGAUAACGACGAAUAUAAUGCUAGACUUUCGCAAGGAUUCACCUUGCAGCCGGGGAGAAAGGGUCGUUGCCGAUGCAACGCGAUGGCAGUCACGCGCAGCUUAGCAUUGAAUCAUUGCGGAUUGGCCGGCCCCGAAUUUAAGGGAGGUCUAUGCGCAAUCCGCGAAAGGCAGAAAAUAGAUUACUGCUUUUUCUUAGCAAAAGGAUAUGAAUAUGGCUCGCAAUCAGAUGGAGCCGCAAAAACACGUGAAAAUACGAUUUUACAACUUGCCGGCCCAUGCGACAUGAAGCCAAAUCCAGUACAAAGUUAUGCUUUUUCUACUAGUACUCUUCCCAACCGCUGUCACCUCAGAAACUAUUUUAUGACCUCACGGGCUUGCGCCUGGGAUGUUUUGCGAGUUCGAACUCCACCUACGGACCGUCCAGAGCCGCCGCGCCUAAAUGUGCGCGGUAGCAACCCGCGCGGCUCGCGGCGUUCACAAUUAAUUGAUCGCCCGGUAGGGGUAACUGUAUGGACAUGCGUUUGCAUGAAAACAGGAGAUAUGGACAAUCGGAAUCCCACCGAUCUACGAAAACCCUGCAAGUAUGGGCUCUACACAAAACUGGACGUUAUACACACACACACUUCGCGCGGGUACAUGCGACGUAUCAUUCUUUUUAGGGAACUUUGGCGCGCCGAUGGCUCUGAACCACGCAACGUGCUACUGGGCUGCACAAGUAGUCACUGUCGUUCACUUGGCCAGAUUUGCUGUGUCAAAUCUGUUCGACACGCCAAUAGGCCGAUAGAAGGGGCUCACAUGAUAAAGUGGGAAAAUUUCCGCACCUGCGAAACUCACGGUCGGCAUCCUUCGCUGCCGACCCAAGCCCAAACACGCACUAAACCGAUAUCCCCGUUGGGCAAAGCAGGCAAGAAAGGUGCGGAGUCCGUAAAGCUACGUUCCACGUCAAACAGAAAAGGGCACAUUACGGGGUUCGAGACGAAUAGGUCGAACGGCCUGGGUCAUCAUCGGCUGAGCUGGACUAGAGUAUCGGACACACCAAAUCACUCGGAGACUCUGAAGAACCCAAUGGAGGUCUCUGGAAAAUCAUUGGUGACACAGGUCGGCAUGGGGAUAGAUCAUGAUCCCAACAGCGUCAGGUUCCCUAGCUUCCUCGGAUUCCAUUCGUUUGGAAUCUUCGAGUACUCCCAGGUGAGUAUCACAAUCGAGCCAUGGAGAAACAUCACGGCGCUUGUUAAUGCAGUCACCGGCUGGCCGAGAGCUGCACAACUUGUUGGAUUCAAGACUCCGGCAACUCUACAACGAACUCACAUCCAGUCGGGGUGGCGGCAUGCGAAGUGUAAAGUCCGAUCCUGUUGCUUAAAAAGUCACCGUCAAGGAAGGUUUCCUGGAGCCCUUCGCGUGUCUUGCCAUCCCACGCAAAACCUGAUGAAAUGCGGUAACCGAUCGUCACUUUGGGAGAUGAAGAUUUCUAUACGAGCGAGUAAGGCUGAUCUCAUUUACGGUGUCCUCUUCAAAUCUCCAAUUACUCCGCAAGGUCGCGUUUCUGUUUCGCUGGUACGUACGGGGGUCUCAGGGGUAAGGGGCACACACCUCAGGGCACUGCCUUCCGUUGCAAAGGUCGGCUUAUUGGUUAUCUGGUUGCACAGCACAGCCGUGUUGCGGUGGUAUAAAAGAGUCAGUGAAUUCCGAUAUAACGACCACACUAUGUACCGCCAACGACAAUGCAGGAUCGCUCGGACCCCCAUGGACCUCCUUGCCGGGCCGUUCAGAUACUGGUCGGCGCCGGAUGUAAAGAUUGUGAGGGGACCUCAGGGUUCGAGAAAAGAUCAAGAGGUUACAGGCUGGGUUGCGAUCCGCAUCGACGAUACUUCGUUGGGCCGAUUUAAGAACCUAGGAACGUUUGGACUGUCGCGCCUACGAGUUAGAGAUGCGUUCGCUUACCGUAAGAUGAAACCCGAGGAUUCCGUGAUGCUUACUACUGGGUGGGUGGGCGUCAUUGCCAAUUUUGCUACCAAUUUGGCAAAGACCAGGGGGACGGUAUGUCGCCGCGCGCCCGAUGGCGGUGCCGGAUUUUAUGUAGCGUGGCUUCUACGUAGGUUUUACCUGAGUAUUCGACGUAGGCUGGACCUAAGGGCACAGCGACGACUAUUGAUACUGUCGGGGAAACAUACCGAUCCGCUAAGUUCUCCCAUAAUCAUCUGUGAGAACUCUAAGGUAAUGUGCGCAAGUAUCACAUGGUUUAAGAGUGCCCUAGCAGGCCUAAUCCGGGAUGUUGGUACCGCCAUUCUGGAUACGUGCAGAAUCCUUGGACAUGUGCUACAAGUGCUGGACCCUCUAAUAGUGGAUACUCGUGCUCCCCAAAGUAGCUUGAUUGGGACGGCGUCAAGUCAUAAGCGGCCCAAAAGCCCGCAUACAUGUCAGUACUGUACUUUUCCGUUCUAUUGGCUUGUGAGGAUGUCCCUGUCACCGUAUUGUGUCGCUAUCUUUUCGGUCAGCCAGUUCGUCGGCGAUCUGAUGGUCAUGAGGUGCAAGAGGUUAGCAUCAAAUGAAGUCGGUCAUGAGUUGAACGCAAACGCGCUGGAGCCUCCUCAGCCUAUCCGUAUGGUUCUACUCCUUGGAUAUGACCUUGGAAGGAAUGGGUCAUGGCAAGCAGCGAAGAGCCAGCGUUACAUAACUCGGGAUUACGAAGCCGCAGCCGCCUUUGGGCGGGUCGUUAGGAAGAUAAGCGCCAGACAAACAUGGCUCCCUUGGUAUACGCCAGAUCGCGCGCGACUUCGCUCAGCUGCCGUAGCGGACUACAUAGCACCUCUCAAUUCCGGGGGGUCUGUCAGCACUAAGGUACUAUAUGCUACUAAGCCUCUAUCGGUUGUACAUACCUUCCAACUGGGGCGGGUUCUAAGCUGCACAUUGUUCCAUAUAAUGUUGGUUUAUGCUGUUGCCAACCCCCACCGCAAGACCAUCGCGGACGUGCCGCGGGUUGCCGAAGACAUCUGCCCAGAUACCGGGUGGGUUUCAUACUCCAGAGGACGAAAACGUCGCGUAGGCCCCUGUUGCCUCUCAAAGUGUAUUUUAAGGACGGGUAUUGGCUCUCAUUUUUAUGGAUAUGUGGUUGCUCGUAUCCGUGAACCCGCCACUCGAAGAAGUCCGUCUCUAGGGUCAUCCAUCAACUCGUACCCUUGGAGAUUUCUACUAAUAAUCAUUCCAUUCAUCCUGUUCGAUGUGAUCCCUCGCUUGAGCCCACUUAGAGCUGAACGAUCAUACCCGCACACAGCUGGCAAUCGUCUGCUUUCAGCCACCGGCCACGUUCAAAGGAGGUCAAUACAGAGUUCGGUUUACGGCAGGGAUGCUCAUGGGCCGUGCUGCAAUCUUGCCCUCGUGGAAGAUGCAAGUUCUACUAGGAUGAGUAGGGGGUUUUACGUCGCCUCGAUGCCAGCAACGUUUCACGAGGACCCACGCGUAUACCCAAGCCAGCUGUUCGAAAGAGGUUUUGCUGGUGAACGUAUUCUCCCAAACACUGCCCCCUCGGGUUUGUGUGAGUUAUUUGCCGUAGUCCCCGGCGACCAUGCCCCAAGGGGGUAUCGUCGACCGACGGCGACGACACCUGGGCCUGAACUCCGAAAGUUCGGACAAUUCGGGGUCUGCAAGAGAUUCUACACAAAAUAUACUCUUAAGGAGUCGCCAGCGGACCCGCACGCAUCUCCUCUGUUCCAAAAGAUAGAGCAGUUGCACUUACCCAUGGUGUUAGCUAUAACGUACUACAGGAGCGCAGCACCACAGACUCUGGAGGCCAAGAGGUUUACCCUGCAACUCAGCCUCCGGGUAGAGAGGCCAUAUCGAAAGUCUUUCUGUGAACAUGACGUCUCUGCAUGGUUUUUGGUCGCAGUUGAAGCCUACCUUGGAAGCUCUAUAGGCAGUACAGGCGGGCGCACCUUAGGUGCGGGAAUGGGCAGCACGGGCUUUAAGGAACCUCCCGAUGCCCCUAAGAUGAACACGCAGACACCAAGGCGGGAGCACUUCCGUGUGCACAAAGUACUUCAGUCGGCGAUAUGA'
#print rna_to_protein(rna_seq)








string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))
