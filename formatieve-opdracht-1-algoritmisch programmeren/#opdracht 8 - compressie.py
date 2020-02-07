def compressie():
    nieuwf = ''
    f = open('Documents/HU-structuredprogramming/formatieve-opdracht-1-algoritmisch programmeren/file.txt', 'r')
    for i in f.readlines():
        i = i.strip(' ', '\t')
        if i == '\n':
            continue
        else:
            nieuwf.append(i)
    f = open('Documents/HU-structuredprogramming/formatieve-opdracht-1-algoritmisch programmeren/file.txt', 'w')
    f.write(nieuwf)
    f.close()
