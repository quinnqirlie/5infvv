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


Prompt:
"File "/Users/quinnknapen/Documents/5infvv/Examen/ExamenOef.py", line 22, in <module> totale_omzet += prijs * verkocht TypeError: can't multiply sequence by non-int of type 'float' wat is dit voor fout"

Antwoord (code):
# verkocht is een lijst, dus eerst optellen met sum()
totaal_verkocht = sum(verkocht)
totale_omzet += prijs * totaal_verkocht

# of in één regel
totale_omzet += prijs * sum(verkocht)