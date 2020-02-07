def verschuiven(ch, n):
    n = int(n)
    ch = list(ch)
    if n > 0:
        while n > 0:
            ch.append(ch[0])
            ch.remove(ch[0])
            n -= 1
        ch = str(ch)
        print(ch)
    elif n == 0:
        ch = str(ch)
        print(ch)
    else:
        while n < 0:
            ch.insert(0, ch[7])
            ch.remove(ch[8])
            n -= 1
        ch = str(ch)
        print(ch)
print(verschuiven(input('geef bitwaarde: '), input('aantal keer verschuiven: ')))