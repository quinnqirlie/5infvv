limiet = int(input("Geef een limiet: "))
teller = 1
priemgetallen = []
print("De priemgetallen zijn: ")
while teller <= limiet:
    restteller = 1
    for i in range(1, teller):
        rest = teller%i
    
        if rest == 0:
            restteller += 1
    
    if restteller == 2:
        print(f"{teller}")   
    
    teller +=1