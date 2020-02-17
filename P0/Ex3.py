from Seq0 import *
from pathlib import Path

print('-----| Exercise 3 |------')

FOLDER = '../Session-04/'
Names = ['U5.txt', 'RNU6_269P.txt', 'FXN.txt', 'ADA.txt']

# for filename in Names:
    # file_contents = Path(FOLDER + filename).read_text()
    # seq_dna = file_contents
    # index_finish = seq_dna.find('\n')
    # seq_dna = seq_dna[index_finish + 1:]
    # seq_dna = seq_dna.replace('\n', '')
    # number_bases = len(seq_dna)
    # print(number_bases)

# print('Gene U5 ---> Length:', seq_len(FOLDER + Names[0]))

print(seq_len(FOLDER + filename))