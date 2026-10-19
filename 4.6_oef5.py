producten = {
    "appel": 0.75,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00,
    "druiven": 2.50,
    "mango": 1.95,
    "ananas": 3.25
}

nieuwe_prijzen = {}
for product, prijs in producten.items():
    nieuwe_prijzen[product] = round(prijs * 1.05, 2)

print(nieuwe_prijzen)

duurder = {}
for product, prijs in producten.items():
    if prijs > 1.50:
        