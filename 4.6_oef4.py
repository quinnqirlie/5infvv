cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}


som = 0
for vak,cijfer in cijfers.items():
    som = som + cijfer

gemiddelde = som / len(cijfers)
gemiddelde = round(gemiddelde,1)

print(gemiddelde)

max = cijfers["Biologie"]
min = cijfers["Nederlands"]
hoogste_vak = ""
laagste_vak = ""
for vak,getal in cijfers.items():
    if max < getal:
        max = getal
        hoogste_vak = vak
    if min > getal:
        min = getal
        laagste_vak = vak

print(f"{max}, {hoogste_vak}")
print(f"{min}, {laagste_vak}")

voldoende = ""
onvoldoende = ""
print(f"Je hebt een voldoende voor:")
for vak, cijfer in cijfers.items():
    if cijfer >= 6:
        voldoende = vak
        print(f"{vak}")

print(f"Je hebt een onvoldoende voor: ")
for vak, cijfer in cijfers.items():
    if cijfer < 6:
        onvoldoende = vak
        print(f"{vak}")

