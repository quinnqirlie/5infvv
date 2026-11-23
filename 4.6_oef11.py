while True:
    getal1 = float(input("Geef het eerste getal: "))
    operator = input("Geef een operator (+,-,*,/): ")
    getal2 = float(input("Geef het eerste getal: "))

    if operator == "+":
        bewerking = getal1 + getal2

    elif operator == "-":
        bewerking = getal1 - getal2

    elif operator == "*":
        bewerking = getal1*getal2

    elif operator == "/":
        bewerking = getal1/getal2
        if getal2 == 0:
            print("Delen door nul is niet mogelijk.")
            bewerking = None

    else:
        print("Deze operator is niet geldig, geef een andere.")

    print(f"{getal1}{operator}{getal2} = {bewerking}.")

    stoppen = input("Wil je graag doorgaan? ").lower
    if stoppen == "nee":
        break