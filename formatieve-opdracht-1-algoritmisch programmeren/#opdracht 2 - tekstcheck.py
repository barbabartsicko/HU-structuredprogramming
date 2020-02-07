lst = [' ', ',', '!', '?']
def tekstcheck():
    x = -1
    str1 = input('geef een string ').lower()
    str2 = input('geef een string ').lower()
    for i in str1:
        x += 1
        if i in lst:
            continue
        elif i != str2[x]:
            print('het eerste verschil zit op index: ' + str(x + 1))
            continue
    print('zinnen zijn identiek')


print(tekstcheck())