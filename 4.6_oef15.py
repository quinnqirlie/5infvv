import random

quiz = {
    "Wat is de hoofdstad van Frankrijk?": {
        "opties": ["A. Londen", "B. Parijs", "C. Berlijn", "D. Rome"],
        "antwoord": "B"
    },
    "Wat is de hoofdstad van Tsjechië?": {
        "opties": ["A. Sofia", "B. Boedapest", "C. Kiëv", "D. Praag"],
        "antwoord": "D"
    },
    "Wat is het kleinste land ter wereld?": {
        "opties": ["A. Malta", "B. Vaticaanstad", "C. San Marino", "D. Andorra"],
        "antwoord": "B"
    },
    "Wat is het meest dichtbevolkt land ter wereld?": {
        "opties": ["A. Monaco", "B. Singapore", "C. Laos", "D. Luxemburg"],
        "antwoord": "A"
    }
}

opnieuw = "ja"

while opnieuw == "ja":

    score = 0
    vragen = list(quiz.keys())
    random.shuffle(vragen)
    
    for i in range(0,len(vragen)):
        vraag = vragen[i]
        print(vraag)

        for optie in quiz[vraag]["opties"]:
            print(optie)

        gok = input("Je antwoord (A, B, C of D): ").upper()
        if gok == quiz[vraag]["antwoord"]:
            print("Juist!")
            score += 1
            print(f"Score = {score}")
            print(" ")

        else:
            print(f"Helaas, het juiste antwoord was {quiz[vraag]['antwoord']}.")
            print(" ")
    print(f"Je eindscore is: {score}")
    verder = input("Wil je nog eens de quiz doen?: ").lower()    
    if verder == "nee":
        break
        