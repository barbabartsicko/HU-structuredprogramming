# gemiddelde van lijst met cijfers
def gemiddelde(lst):
    return sum(lst) / (len(lst))

# gemiddelde van lijst van lijsten
def lstgemiddelde(lst):
    totaal = 0
    lengte = 0
    for i in lst:
        totaal += sum(i)
        lengte += len(i)
    return totaal / lengte
