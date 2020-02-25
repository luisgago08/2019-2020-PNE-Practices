from Seq0 import *

FOLDER = '../Session-04/'
Names = ['U5.txt', 'RNU6_269P.txt', 'FXN.txt', 'ADA.txt']

print('-----| Exercise 3 |------')

for gene in Names:
    seq = seq_read_fasta(FOLDER + gene)
    print(f"Gene {gene} ---> Length: {seq_len(seq)}")
