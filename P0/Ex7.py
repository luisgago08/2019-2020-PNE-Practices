from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5', 'RNU6_269P', 'FXN', 'ADA', 'FRAT1']
Bases = ['A', 'C', 'T', 'G']
txt = '.txt'

print('-----| Exercise 7 |------')
GENE = Names[0]
print(f"Gene {GENE}:")
seq = seq_read_fasta(FOLDER + Names[0] + txt)[:20]
rev = seq_complement(seq)
print(f"Frag: {seq}")
print(f"Comp: {rev}")