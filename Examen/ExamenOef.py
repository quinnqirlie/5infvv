producten = {
    "burger":    {"prijs": 9.50, "variabele_kost": 4.20, "verkocht": [120, 95, 140, 110]},
    "frietjes":  {"prijs": 4.00, "variabele_kost": 1.10, "verkocht": [200, 180, 230, 190]},
    "wrap":      {"prijs": 7.50, "variabele_kost": 3.60, "verkocht": [60, 45, 70, 55]},
    "frisdrank": {"prijs": 2.50, "variabele_kost": 0.80, "verkocht": [150, 130, 170, 160]},
}
vaste_kosten_per_maand = 2400.0

while True:
    def omzet_per_week(producten, week):
        # week 0 = eerste week, 1 = tweede week, ...
        weektotaal = 0
        for eten, info in producten.items():
            # neem van elk product het getal van die week uit de lijst
            weektotaal += info["prijs"] * info["verkocht"][week]
        return weektotaal

    def hoogste_laagste_week(producten):
        aantal_weken = len(producten["burger"]["verkocht"])
        weekomzetten = [omzet_per_week(producten, week) for week in range(aantal_weken)]
        #for lus om hoogste en laagste te zoeken

        hoogst = weekomzetten[0]
        laagst = weekomzetten[0]
        beste_week = 0       #index beste week
        slechtste_week = 0   # index van de slechtste week

        for week in range(aantal_weken):
            omzet = weekomzetten[week]
            if omzet > hoogst:
                hoogst = omzet
                beste_week = week
            if omzet < laagst:
                laagst = omzet
                slechtste_week = week

        #+1, zodat je het weeknummer in mensentaal hebt
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
            prijs = info["prijs"] #makkelijkere benamingen om als variabele te gebruiken
            variabele_kost = info["variabele_kost"]

            contributiemarge = prijs - variabele_kost #winst berekenen
            procent = round(contributiemarge / prijs * 100, 2)

        print(f"{eten}: €{contributiemarge} -> {procent}%")

    if keuze == "2":
        totale_omzet = 0
        totale_variabele_kost = 0 #om in de for lus alles samen te tellen

        for eten, info in producten.items():
            prijs = info["prijs"]
            variabele_kost = info["variabele_kost"]
            verkocht = info["verkocht"]
            totaal_verkocht = sum(verkocht) #afzet van 4 weken per product

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