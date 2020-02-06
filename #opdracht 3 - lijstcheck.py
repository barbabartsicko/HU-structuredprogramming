# A.
def count(lst):
    x = input('kies getal ')
    count = 0
    for i in lst:
        if int(x) == i:
            count += 1
        else:
            continue
    print(str(x) + ' komt ' + str(count) + ' keer voor in de lijst')


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

print(grootsteverschil([2, 3, 1, 7, 4, 1, 12, 9,]))