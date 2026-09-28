hoogte = int(input("Geef de hoogte: "))
rij = []

for rij in range(1, hoogte+1): 
    regel = ""
    for i in range(rij):
        regel = regel + "*"
    print(regel)