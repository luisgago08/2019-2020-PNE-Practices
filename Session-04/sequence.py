from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()

seq_dna = file_contents
index_finish = seq_dna.find('\n')
seq_dna = seq_dna[index_finish + 1:]
seq_dna = seq_dna.replace('\n', '')
number_bases = len(seq_dna)

print(number_bases)
