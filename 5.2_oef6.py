def even_getallen(getallen):
    even_getallen = []
    for getal in getallen:
        rest = getal % 2
        if rest == 0:
            even_getallen.append(getal)
    return even_getallen

lijst = [2,6,4,5,22,33,19]
getallen = even_getallen(lijst)
print(getallen)