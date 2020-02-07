#bibliotheekfunctie
def palindroom1(str):
    str = str.casefold()
    revstr = reversed(str)
    if list(str) == list(revstr):
        print('het is een palindroom')
    else:
        print('het is geen palindroom')

#zelf omdraaien
def palindroom2(str):
    str = str.casefold()
    revstr = str[::-1]
    if list(str) == list(revstr):
        print('het is een palindroom')
    else:
        print('het is geen palindroom')

