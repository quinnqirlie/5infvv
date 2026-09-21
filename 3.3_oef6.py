jaartal = int(input("Voer een jaartal in: "))
if jaartal % 4 == 0  and jaartal % 100 != 0  or jaartal % 400 == 0:
    print("Dit jaar is een schrikkeljaar.")

else:
    print("Dit jaar is geen schrikkeljaar.")