hoogte = int(input("Geef de hoogte: "))
breedte = int(input("Geef de breedte: "))

for rij in range(hoogte): 
    regel = ""
    for kolom in range(breedte):
          regel = regel + "*"
    print(regel)