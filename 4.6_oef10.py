print(" - Minimaal 8 karakters lang")
print(" - Bevat ten minste één hoofdletter")
print(" - Bevat ten minste één cijfer")
print(" - Bevat ten minste één speciaal karakter (bijv. !@#$%^&*")
    
speciale_tekens = "!@#$%^&"
while True:
    
    wachtwoord = input("Voer je gewenst wachtwoord in : ")

    if len(wachtwoord) < 8:
         print("Wachtwoord is te kort, probeer opnieuw met minimum 8 karakters.")
         

    if not any([teken.isupper()for teken in wachtwoord]):
        print("Gebruik min. 1 hoofdletter. Probeer opnieuw.")

    if not any([teken.isdigit() for teken in wachtwoord]):
        print("Gebruik min. 1 cijfer. Probeer opnieuw.")

    
    if not any([teken in speciale_tekens for teken in wachtwoord]):
            print("Gebruik min. 1 speciaal teken. Probeer opnieuw.")

    else:
        print("Wachtwoord ingesteld")
        break

    
    
