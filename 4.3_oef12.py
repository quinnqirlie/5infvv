aantal_studenten = int(input("Hoeveel leerlingen zijn er?: "))
namen = []
cijfers = []

for i in range(aantal_studenten):
    naam = input(f"Geef de naam van de student {i + 1}: ")
    namen.append(naam)
    cijfer = float(input(f"Geef het cijfer van de student {i + 1}: "))
    cijfers.append(cijfer)
som = 0
for i in range(0,aantal_studenten):
    som = som + cijfers[i]


gemiddelde = som / aantal_studenten
print(gemiddelde)

for i in range(aantal_studenten):
    if cijfers[i] > gemiddelde:
        print(f"De leerling {namen[i]} heeft boven het gemiddelde.")