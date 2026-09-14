budget= 50
boek= 12.50
tijdschrift = 3.75
prijs_alles = 2*boek + 3*tijdschrift
overhouden= budget-prijs_alles
overhouden_afgerond = round(overhouden,2)
print( f"Na het kopen van 2 boeken en 3 tijdschriften heb ik nog {overhouden_afgerond} over.")