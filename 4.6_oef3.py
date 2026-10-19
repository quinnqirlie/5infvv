telefoonboek = {}

afgesloten = False

for beurt in range(100):
    
    if not afgesloten:

        print(" telefoonboek menu")
        print("1.contact toevoegen")
        print("2.Conact opzoeken")
        print("3.contact verwijderen")
        print("4.alle contacten weergeven")
        print("5.afsluiten ")
                
        keuze = input("kies een optie(1 -5): ")
        
        if keuze == "1":
            naam = input("Geef de naam van je nieuwe contact: ")   
            nummer = input("Geef het nummer van je nieuwe contact: ")
            telefoonboek [naam] = nummer
            print("Contact toegevoegd")



        if keuze == "2":

            naam = input("Welk contact wil je opzoeken? ")

            if naam in telefoonboek:

                print(f"{naam}: {telefoonboek[naam]}")

            else:

                print("Contact niet gevonden")



        if keuze == "3":
            naam = input("Geef de naam die je wilt verwijderen:")
            if naam in telefoonboek:
                del telefoonboek[naam]

            else:

                print("Contact niet gevonden")



        if keuze == "4":
            if len(telefoonboek) == 0:
                print("Telefoonboek is leeg")
            else:
                print(f"Telefoonboek:")
                for naam,nummer in telefoonboek.items():
                    print(f"{naam}: {nummer}")

    

        if keuze == "5":

            print("Tot ziens")

            afgesloten = True

    else:

        print("Je hebt een ongeldige keuze ingegeven. Geef een cijfer van 1 t.e.m. 5.")