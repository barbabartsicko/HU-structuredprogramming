import random
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def randomnr():
    x = input('kies een nummer van 1 t/m 9: ')
    nr = random.choice(lst)
    if int(x) == nr:
        print('goed gegokt ')
    else:
        return randomnr()
