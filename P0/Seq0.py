from pathlib import Path


def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace('\n', '')
    seq_dna = seq_dna[:20]
    return seq_dna


def seq_len(list):
    for element in list:
        element = element + '.txt'
        file_contents = Path(element).read_text()
        seq_dna = file_contents
        index_finish = seq_dna.find('\n')
        seq_dna = seq_dna[index_finish + 1:]
        seq_dna = seq_dna.replace('\n', '')
        number_bases = len(seq_dna)
        return number_bases
