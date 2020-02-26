from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5', 'RNU6_269P', 'FXN', 'ADA', 'FRAT1']
Bases = ['A', 'C', 'T', 'G']
txt = '.txt'
print('-----| Exercise 5 |------')

for gene in Names:
    seq = seq_read_fasta(FOLDER + gene + txt)
    print(f"Gene {gene}: {seq_count(seq)}")