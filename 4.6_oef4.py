cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}

for punt in cijfers:
    som = punt + som

gemiddelde = som / len(cijfers)

print(gemiddelde)