getallen = list(range(1,21))
even = []
oneven = []
for getal in getallen:
    if getal %2 == 0:
        even.append(getal)

    else:
        oneven.append(getal)

print(even)
print(oneven)