bedrag = float(input("Hoeveel euro heb je gespendeerd?: "))
if bedrag > 100:
    print(f"Je krijgt 10% korting.")
    EindPrijs = bedrag * 0.9
    rounded = round(EindPrijs,2)
    print(f"Het uitendelijke bedrag is {rounded} euro.")

elif bedrag > 50:
    print(f"Je krijgt 5% korting. ")
    EindPrijs2 = bedrag * 0.95
    rounded2 = round(EindPrijs2,2)
    print(f"Het uiteindelijke bedrag is {rounded2} euro.")

else:
    print(f"Je krijgt geen korting, je eindbedrag is {bedrag} euro.")