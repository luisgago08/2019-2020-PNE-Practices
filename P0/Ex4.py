from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5.txt', 'RNU6_269P.txt', 'FXN.txt', 'ADA.txt']
Bases = ['A', 'C', 'T', 'G']

print('-----| Exercise 4 |------')

for gene in Names:
    seq = seq_read_fasta(FOLDER + gene)
    print()
    print(f"Gene {gene}:")
    for base in Bases:
        print(f"  {base}: {seq_count_base(seq, base)}")