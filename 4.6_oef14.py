while True:
    import random
    lijst = ["appel", "boom", "citroen", "diamant", "ergens", "fazant"]
    woord = random.choice(lijst)
    lengte = len(woord)
    visueel = "_" * lengte
    print(visueel)
    levens = 6
    print(f"Levens: {levens}")
    gok = input("Raad een letter: ").lower
    if gok in woord:
        print("Goed geraden!")

    else:
        print(f"Helaas, de letter {gok} komt niet voor in het woord.")
        print(visueel)
        levens - 1
        print(f"Levens: {levens}")
    break