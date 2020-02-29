from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5', 'RNU6_269P', 'FXN', 'ADA', 'FRAT1']
Bases = ['A', 'C', 'T', 'G']
txt = '.txt'

print('-----| Exercise 8 |------')

for gene in Names:
    seq = seq_read_fasta(FOLDER + gene + txt)
    d = seq_count(seq)
    # -- Create a list with all the values
    ll = list(d.values())
    # -- Calculate the maximum
    m = max(ll)
    print(f"Gene {gene} most frequent base is: {Bases[ll.index(m)]}")