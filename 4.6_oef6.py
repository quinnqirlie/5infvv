woordenboek = {
    "hallo": {"Engels": "hello", "Frans": "bonjour", "Spaans": "hola"},
    "maar": {"Engels": "but", "Frans": "mais", "Spaans": "pero"},
    "school" : {"Engels": "School", "Frans": "école", "Spaans": "escuela"}
}

gevraagd = input("Van welk Nederlands woord wil je de vertaling?: ").lower().strip()
doeltaal = input("Wat is de doeltaal? Engels, Frans, Spaans?: ").capitalize()
vertaling = woordenboek[gevraagd][doeltaal]

if gevraagd in woordenboek.keys():
    
    if doeltaal in woordenboek[gevraagd].keys():
        print(f"De vertaling van {gevraagd} is {woordenboek[gevraagd][doeltaal]}.")
    else:
        print("Deze taal zit niet in het woordenboek")

else:
    print(f"{gevraagd} zit niet in het woordenboek.")
woordenboek[gevraagd][doeltaal] = doeltaal
