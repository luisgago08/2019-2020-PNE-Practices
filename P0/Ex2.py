from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = 'U5.txt'

print('DNA file:', FILENAME)
seq = seq_read_fasta(FOLDER + FILENAME)
print('The first 20 bases are: ')
print(seq[0:20])
