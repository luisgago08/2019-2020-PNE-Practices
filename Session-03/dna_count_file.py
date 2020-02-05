with open('dna.txt') as f:
    total = 0
    a = 0
    c = 0
    t = 0
    g = 0
    for line in f:
        for character in line:
            total = total + 1
            if character == 'A':
                a += 1
            elif character == 'C':
                c += 1
            elif character == 'T':
                t += 1
            elif character == 'G':
                g += 1

    print('Total length: ', total, "\nA: ", a, '\nC: ', c, '\nT: ', t, '\nG: ', g)
