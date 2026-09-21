voornaam= input("Geef je voornaam:")
achternaam= input("Geef je achternaam:")
functie = input("Wat is je functietitel?:")

naam = f"{voornaam} {achternaam}".upper()

#breedte bepalen op basis van de langste regel (+marge van 2 spaties links/rechts)
breedte= max(len(naam), len(functie)) + 4

rand = "+" + "-" * breedte + "+"
regel_naam = "|" + naam.center(breedte) + "|"
regel_functie = "|" + functie.center(breedte) + "|"

print(rand)
print(regel_naam)
print(regel_functie)
print(rand)