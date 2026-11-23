levens = 6
import random
lijst = ["appel", "boom", "citroen", "diamant", "ergens", "fazant"]
woord = random.choice(lijst)
visueel = ["_"] * len(woord)
while True:
    print(" ".join(visueel))    
    print(f"Levens: {levens}")
    gok = input("Raad een letter: ").lower()

    if len(gok) == 1 and gok.isalpha():

        if gok in woord:
                    for index, letter in enumerate(woord):
                        if letter == gok:
                            print("Goed geraden!")
                            visueel[index] = gok
        
        else:
            print(f"Helaas, de letter '{gok}' komt niet voor in het woord.")
            levens = levens - 1
        
        print(" " * 20)
        
            
        if "_" not in visueel:
            print(f"Je hebt het woord {woord} geraden!")
            break
        
        if levens == 0:
            print("Spijtig. Je levens zijn op. Speel nog eens.")
            break


    else:
        print("Geen geldige invoer! Geef enkel één letter in.")


