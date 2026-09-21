getal = int(input("Voer een getal van 1 - 100 in: "))
range = range(1,100)
if getal in range:
    print("Het getal zit in de interval.")

else:
    print("Het getal ligt buiten het interval.")