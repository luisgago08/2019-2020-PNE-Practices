import http.client
import json
from Seq1 import Seq

sequence_id = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

for key1 in sequence_id:

    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id"
    GENE = "/" + sequence_id[key1]
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + GENE + PARAMS

    print()
    print(f"SERVER: {SERVER}")
    print(f"URL: {URL}")

    # -- CONNECTING

    conn = http.client.HTTPConnection(SERVER)

    # -- MESSAGING

    try:
        conn.request("GET", ENDPOINT + GENE + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- READING RESPONSE
    r1 = conn.getresponse()

    # -- STATUS LINE
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- DECODING
    data1 = r1.read().decode("utf-8")

    # -- CREATING A VARIABLE WITH THE DATA
    # -- CREATING A VARIABLE WITH THE DATA
    gene = json.loads(data1)

    # Print the information in the object
    print()
    print("Gene: ", end="")
    print(sequence_id[key1])

    print("Description: ", end="")
    print(gene["desc"])

    gene_seq = gene["seq"]
    seq = Seq(gene_seq)
    seq_length = len(gene_seq)

    print("Total length: ", end="")
    print(seq_length)
    number_of_A = seq.count_base("A")
    percentage_A = "{:.1f}".format(100 * number_of_A / seq_length)
    number_of_G = seq.count_base("G")
    percentage_G = "{:.1f}".format(100 * number_of_G / seq_length)
    number_of_T = seq.count_base("T")
    percentage_T = "{:.1f}".format(100 * number_of_T / seq_length)
    number_of_C = seq.count_base("C")
    percentage_C = "{:.1f}".format(100 * number_of_C / seq_length)

    print("A", end="")
    print(f": {number_of_A} ({percentage_A}%)")
    print("C", end="")
    print(f": {number_of_C} ({percentage_C}%)")
    print("G", end="")
    print(f": {number_of_G} ({percentage_G}%)")
    print("T", end="")
    print(f": {number_of_T} ({percentage_T}%)")

    value = 0
    base = ""
    for e, b in (seq.count()).items():
        # se empieza en 0, cada vez que va apareciendo una base se va sumando y queda ese valor como el mínimo
        while b > value:
            value = b
            base = e
    print("Most frequent Base: ", end="")
    print(base)