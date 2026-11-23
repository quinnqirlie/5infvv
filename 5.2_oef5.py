def vind_maximum(getallen):
    maximum = getallen[0]
    for getal in getallen:
        if getal > maximum:
            maximum = getal
    return maximum

lijst = [14, 99, 5, 14, 66, 20]
print(vind_maximum(lijst))
print(vind_maximum([-9,8,6,14,37]))