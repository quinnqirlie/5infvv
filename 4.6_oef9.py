import random

geheim_getal = random.randint(1, 100)

print("Raad het geheime getal tussen 1 en 100!")

while True:
    gok = (input("Jouw gok: "))
    

    if gok.lower() == "q":
        break

    gok = int(gok)

    if gok < geheim_getal:
        print("Te laag!")
    elif gok > geheim_getal:
        print("Te hoog!")
    else:
        print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden.")
        break
