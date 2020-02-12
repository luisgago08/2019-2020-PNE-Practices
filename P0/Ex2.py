from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = 'U5.txt'

print('DNA file:', FILENAME)
print('The first 20 bases are: ')
print(seq_read_fasta(FOLDER + FILENAME))
