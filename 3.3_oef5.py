cijfer = int(input("Wat is je cijfer?: "))
aanwezigheid = int(input("Wat is je aanwezigheid in procent?: "))

if cijfer >= 50 and aanwezigheid >= 80:
    print (f"Gefeliciteerd, je bent geslaagd!")
else:
    print(f"Helaas, je bent gezakt.")