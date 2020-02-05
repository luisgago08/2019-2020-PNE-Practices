dna_seq = str(input("Enter a DNA sequence: "))

total = 0
a = 0
c = 0
t = 0
g = 0
for i in dna_seq:
    total = total + 1
    if i == 'a':
        a += 1
    elif i == 'c':
        c += 1
    elif i == 't':
        t += 1
    elif i == 'g':
        g += 1

print('Total length: ',total,"\nA: ", a,'\nC: ',c,'\nT: ',t,'\nG: ',g)
