woorden = []

zin = input("Voer een zin in: ")
for woord in zin.lower().split():
    woorden.append(woord.strip(",.;:?!"))

frequentie = {}
for woord in woorden:
    if woord in frequentie:
        frequentie[woord] += 1
    else:
        frequentie[woord] = 1

print(frequentie)