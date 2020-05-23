import http.client
import json
from Seq1 import Seq

Genes = {
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
user_input = input("Write the gene name:")

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
GENE = "/" + Genes[user_input]
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + GENE + PARAMS

Genes = {
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
response = json.loads(data1)

print("GENE: ", end="")
print(user_input)

print("DESCRIPTION: ", end="")
print(response['desc'])

s = Seq(response['seq'])
dictionarycount = s.count
length = s.len()

print(f"Total length:", end="")
print(length)
for key in dictionarycount:
    print(key, end=":")
    average = (int(dictionarycount[key]) / length) * 100
    potato = f" {dictionarycount[key]} ({round(average, 1)}%)"
    print(potato)

listvalues = list(dictionarycount.values())
maximum = max(listvalues)
print("Most frequent base", end=":")

for key,value in dictionarycount.items():
    if value == maximum:
        print(key)