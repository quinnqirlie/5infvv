27/11:
Prompt:
"laat mij deze code kopieren maar zorg dat voor elk stuk zo berekening enzo de juiste if keuze == "1" etc. ervoor staat en dat de tabs kloppen zodat het werkt" (met mijn code met menu)

Antwoord (code):
producten = {
    "burger":    {"prijs": 9.50, "variabele_kost": 4.20, "verkocht": [120, 95, 140, 110]},
    "frietjes":  {"prijs": 4.00, "variabele_kost": 1.10, "verkocht": [200, 180, 230, 190]},
    "wrap":      {"prijs": 7.50, "variabele_kost": 3.60, "verkocht": [60, 45, 70, 55]},
    "frisdrank": {"prijs": 2.50, "variabele_kost": 0.80, "verkocht": [150, 130, 170, 160]},
}
vaste_kosten_per_maand = 2400.0

while True:
    def omzet_per_week(producten, week):
        weektotaal = 0
        for eten, info in producten.items():
            weektotaal += info["prijs"] * info["verkocht"][week]
        return weektotaal

    def hoogste_laagste_week(producten):
        aantal_weken = len(producten["burger"]["verkocht"])
        weekomzetten = [omzet_per_week(producten, week) for week in range(aantal_weken)]

        hoogst = weekomzetten[0]
        laagst = weekomzetten[0]
        beste_week = 0
        slechtste_week = 0

        for week in range(aantal_weken):
            omzet = weekomzetten[week]
            if omzet > hoogst:
                hoogst = omzet
                beste_week = week
            if omzet < laagst:
                laagst = omzet
                slechtste_week = week

        return beste_week +1, hoogst, slechtste_week +1, laagst

    print(" ")
    print("Food Truck Menu:")
    print("1. Contributiemarge weergeven")
    print("2. Maandresultaat weergeven")
    print("3. Break-evenpunt van burgers weergeven")
    print("4. Weekomzetten weergeven")
    print("5. Nieuw product toevoegen")
    print("6. Prijs van product aanpassen")
    print("7. Afsluiten")
    keuze = input("Kies een optie (1-7): ")

    if keuze == "1":
        print("De contributiemarge / winst per product is:")
        for eten, info in producten.items():
            prijs = info["prijs"]
            variabele_kost = info["variabele_kost"]

            contributiemarge = prijs - variabele_kost
            procent = round(contributiemarge / prijs * 100, 2)

        print(f"{eten}: €{contributiemarge} -> {procent}%")

    if keuze == "2":
        totale_omzet = 0
        totale_variabele_kost = 0

        for eten, info in producten.items():
            prijs = info["prijs"]
            variabele_kost = info["variabele_kost"]
            verkocht = info["verkocht"]
            totaal_verkocht = sum(verkocht)

            totale_omzet += prijs * totaal_verkocht
            totale_variabele_kost += variabele_kost * totaal_verkocht
            totale_kosten = totale_variabele_kost + vaste_kosten_per_maand
            winst = totale_omzet - totale_kosten

        print(" ")
        print("Maandresultaat:")
        print(f"Omzet: {totale_omzet}")
        print(f"Variabele kosten: {totale_variabele_kost}")
        print(f"Vaste kosten: {vaste_kosten_per_maand}")
        print(f"Je hebt {winst} euro winst.")

    if keuze == "3":
        break_even = round(vaste_kosten_per_maand /producten["burger"]["prijs"],0)
        print(f"Je moet {break_even} burgers verkopen om je vaste kosten te dekken.")

    if keuze == "4":
        print(" ")
        print("Je totale omzet per week is:")
        print(f"Week 1: {omzet_per_week(producten, 0)}")
        print(f"Week 2: {omzet_per_week(producten, 1)}")
        print(f"Week 3: {omzet_per_week(producten, 2)}")
        print(f"Week 4: {omzet_per_week(producten, 3)}")
        beste_week, hoogst, slechtse_week, laagst = hoogste_laagste_week(producten)
        print(f"Week met hoogste omzet: {beste_week} met {hoogst} euro.")
        print(f"Week met laagste omzet: {slechtse_week} met {laagst} euro.")

    if keuze == "7":
        break

27/11:
Prompt:
"Kan je om de totale omzet per week te bereken een functie hiervoor gebruiken?"

Antwoord (code):
def omzet_per_week(producten, week):
    totaal = 0
    for eten, info in producten.items():
        totaal += info["prijs"] * info["verkocht"][week]
    return totaal

aantal_weken = len(producten["burger"]["verkocht"])

for week in range(aantal_weken):
    omzet = omzet_per_week(producten, week)
    print(f"Week {week + 1}: €{omzet:.2f}")

# weekomzetten in een lijst
weekomzetten = [omzet_per_week(producten, week) for week in range(aantal_weken)]
print(sum(weekomzetten))
print(max(weekomzetten))


23/11:
Prompt:
"hoe kan ik zorgen da ik bij nieuwe dingen bv totale variabele kosten niet weeral heel die for moet doen? is het anders nie zo gek met die print daartussen"

Antwoord (code):totaal_omzet = 0
totaal_variabele_kost = 0

print("De contributiemarge / winst per product is:")
for eten, info in producten.items():
    prijs = info["prijs"]
    variabele_kost = info["variabele_kost"]
    totaal_verkocht = sum(info["verkocht"])

    contributiemarge = prijs - variabele_kost
    procent = round(contributiemarge / prijs * 100, 2)
    print(f"{eten}: €{contributiemarge:.2f} -> {procent}%")

    totaal_omzet += prijs * totaal_verkocht
    totaal_variabele_kost += variabele_kost * totaal_verkocht

winst = totaal_omzet - totaal_variabele_kost - vaste_kosten_per_maand

print(" ")
print("Maandresultaat:")
print(f"Omzet: €{totaal_omzet:.2f}")
print(f"Variabele kosten: €{totaal_variabele_kost:.2f}")
print(f"Vaste kosten: €{vaste_kosten_per_maand:.2f}")
print(f"Winst: €{winst:.2f}")

23/11:
Prompt:
"File "/Users/quinnknapen/Documents/5infvv/Examen/ExamenOef.py", line 22, in <module> totale_omzet += prijs * verkocht TypeError: can't multiply sequence by non-int of type 'float' wat is dit voor fout"

Antwoord (code):
# verkocht is een lijst, dus eerst optellen met sum()
totaal_verkocht = sum(verkocht)
totale_omzet += prijs * totaal_verkocht

# of in één regel
totale_omzet += prijs * sum(verkocht)


Prompt:
"Hoe moet je rekenen met een geneste dictionary waar binnen een key een lijst zit waar je om de beurt een van die getallen moet gebruiken om te rekenen in python"

Antwoord (code):
data = {
    "appel": {"prijs": 1.50, "kost": 0.80, "verkocht": [10, 20, 15, 5]},
    "brood": {"prijs": 2.20, "kost": 1.10, "verkocht": [8, 12, 6, 9]},
}

# geneste lus: om de beurt elk getal uit de lijst gebruiken
for eten, info in data.items():
    prijs = info["prijs"]
    kost = info["kost"]
    for aantal in info["verkocht"]:
        winst = (prijs - kost) * aantal
        print(eten, aantal, winst)

# totaal per eten
for eten, info in data.items():
    totaal_verkocht = sum(info["verkocht"])
    totale_winst = (info["prijs"] - info["kost"]) * totaal_verkocht
    print(f"{eten}: {totaal_verkocht} verkocht, winst {totale_winst:.2f}")
