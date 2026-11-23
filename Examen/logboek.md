Prompt:
"En als je zo'n geneste dictionary waar binnen een key een lijst zit waar je om de beurt een van die getallen moet gebruiken om te rekenen"

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


