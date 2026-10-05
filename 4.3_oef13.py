zin = input("Voer een zin in: ")
woorden = zin.lower().split()

lijst = []

for woord in woorden:
    if woord not in lijst:
        lijst.append(woord)

for uniek in lijst:
    teller = 0
    for woord in woorden:
        if woord == uniek:
            teller = teller + 1

    print(f"{uniek}: {teller}")