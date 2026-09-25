aantal = int(input("Hoeveel getallen wil je invoeren? "))

getallen = []
for i in range(1, aantal + 1):
    getal = float(input(f"Voer getal {i} in: "))
    getallen.append(getal)

gemiddelde = sum(getallen) / len(getallen)
print(f"Het gemiddelde is: {gemiddelde:.2f}")