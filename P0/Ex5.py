from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5.txt', 'RNU6_269P.txt', 'FXN.txt', 'ADA.txt', 'FRAT1.txt']
Bases = ['A', 'C', 'T', 'G']

print('-----| Exercise 5 |------')
for gene in Names:
    seq = seq_read_fasta(FOLDER + gene)
    print(f"Gene {gene}: {seq_count(seq)}")