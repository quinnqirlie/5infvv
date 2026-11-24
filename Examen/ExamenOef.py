producten = {
    "burger":    {"prijs": 9.50, "variabele_kost": 4.20, "verkocht": [120, 95, 140, 110]},
    "frietjes":  {"prijs": 4.00, "variabele_kost": 1.10, "verkocht": [200, 180, 230, 190]},
    "wrap":      {"prijs": 7.50, "variabele_kost": 3.60, "verkocht": [60, 45, 70, 55]},
    "frisdrank": {"prijs": 2.50, "variabele_kost": 0.80, "verkocht": [150, 130, 170, 160]},
}
vaste_kosten_per_maand = 2400.0

totale_omzet = 0
totale_variabele_kost = 0 #om in de for lus alles samen te tellen

print("De contributiemarge / winst per product is:")
for eten, info in producten.items():
    prijs = info["prijs"] #makkelijkere benamingen om als variabele te gebruiken
    variabele_kost = info["variabele_kost"]
    verkocht = info["verkocht"]
    totaal_verkocht = sum(verkocht) #afzet van 4 weken per product

    contributiemarge = prijs - variabele_kost #winst berekenen
    procent = round(contributiemarge / prijs * 100, 2)
    print(f"{eten}: €{contributiemarge} -> {procent}%")

    totale_omzet += prijs * totaal_verkocht
    totale_variabele_kost += variabele_kost * totaal_verkocht

print(" ")
print("Maandresultaat:")
print(f"Omzet: {totale_omzet}")
print(f"Variabele kosten: {totale_variabele_kost}")
print(f"Vaste kosten: {vaste_kosten_per_maand}")