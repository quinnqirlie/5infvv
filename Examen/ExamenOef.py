producten = {
    "burger":    {"prijs": 9.50, "variabele_kost": 4.20, "verkocht": [120, 95, 140, 110]},
    "frietjes":  {"prijs": 4.00, "variabele_kost": 1.10, "verkocht": [200, 180, 230, 190]},
    "wrap":      {"prijs": 7.50, "variabele_kost": 3.60, "verkocht": [60, 45, 70, 55]},
    "frisdrank": {"prijs": 2.50, "variabele_kost": 0.80, "verkocht": [150, 130, 170, 160]},
}
vaste_kosten_per_maand = 2400.0


print("De contributiemarge / winst per product is:")
for eten, info in producten.items():
    prijs = info["prijs"] #makkelijkere benamingen om als variabele te gebruiken
    variabele_kost = info["variabele_kost"]
    verkocht = info["verkocht"]

    contributiemarge = prijs - variabele_kost #winst berekenen
    procent = contributiemarge / prijs * 100 #in procent
    procent = round(procent,2)
    print(f"{eten}: €{contributiemarge} -> {procent}%")


print(" ")
totaal_omzet = 0
print("Maandresultaat:")
for eten, info in producten.items():
    for aantal in info["verkocht"]:
        omzet = info["prijs"] * aantal
        totaal_omzet += omzet
print(f"Omzet: {totaal_omzet}")