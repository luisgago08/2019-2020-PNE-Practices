from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5.txt', 'RNU6_269P.txt', 'FXN.txt', 'ADA.txt', 'FRAT1.txt']
Bases = ['A', 'C', 'T', 'G']

print('-----| Exercise 6 |------')
GENE = Names[0]
print(f"Gene {GENE}:")
seq = seq_read_fasta(FOLDER + Names[0])[:20]
rev = seq_reverse(seq)
print(f"Frag: {seq}")
print(f"Rev : {rev}")
