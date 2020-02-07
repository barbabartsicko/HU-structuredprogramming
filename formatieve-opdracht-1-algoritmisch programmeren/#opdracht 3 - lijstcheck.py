# A.
lst = [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
def count():
    x = input('kies getal ')
    count = 0
    for i in lst:
        if int(x) == i:
            count += 1
        else:
            continue
    return count


# B.
def grootsteverschil(lst):
    verschil = 0
    i = 0
    while i < len(lst) - 1:
        diff = lst[i] - lst[i + 1]
        if verschil < abs(diff):
            verschil = abs(diff)
        i += 1
    print('het grootste verschil is ' + str(verschil))

# C.
def lijst():
    aantal0 = count()
    aantal1 = count()
    if aantal0 > 12:
        print('lijst voldoet niet aan de eisen')
    elif aantal1 <= aantal0:
        print('lijst voldoet niet aan de eisen')
    else:
        print('lijst voldoet aan de eisen')
