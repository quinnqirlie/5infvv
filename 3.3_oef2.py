leeftijd = int(input("Hoe oud ben je?: "))
volwassene = input("Ben je met een volwassene?: ").strip().lower()

if leeftijd >= 16 or volwassene == "ja":
    print("Je mag naar de film.")

else:
    print("Je mag niet naar de film.")