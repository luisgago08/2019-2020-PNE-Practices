from pathlib import Path

# Ex1
def seq_ping():
    print("OK!")

# Ex2
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace('\n', '')
    # seq_dna = seq_dna[:20] # Para que vaya hasta la base 20
    return seq_dna

# Ex3
def seq_len(filename):
    return len(filename)

# Ex4
def seq_count_base(seq, base):
    return seq.count(base)

# Ex5
def seq_count(seq):
    dict = {"A":seq_count_base(seq, "A"), "T":seq_count_base(seq, "T"), "C":seq_count_base(seq, "C"), "G":seq_count_base(seq, "G"), }
    return dict

# Ex6
def seq_reverse(seq):
    return seq[::-1]

# Ex7
#def seq_complement(seq):
    #dict = {"A": "T", "T": "A", "C": "G", "G": "C", }
    #com_seq = ""
    #for element in seq:
