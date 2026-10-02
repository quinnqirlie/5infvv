lijst = []
priemgetallen = []

for i in range(1,51):
    lijst.append(i)

for getal in lijst:
    aantal_delers = 0
    for deler in range(1,getal + 1):
        if getal % deler == 0:
            aantal_delers = aantal_delers + 1
         

    if aantal_delers == 2:
      priemgetallen.append(getal)

print(priemgetallen)