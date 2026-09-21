import random
geheim= random.randint(1, 10)

gok = int(input("Raad het geheime nummer tussen 1-10: "))

if gok == geheim:
    print("Je hebt het nummer juist!")
else:
    print("Sorry dat is niet juist, probeer het nog eens.")