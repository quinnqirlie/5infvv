#vaste wisselkoers: 1 EUR = 1.15 USD op 18/09/2026
WISSELKOERS_EUR_NAAR_USD = 1.15

bedrag= float(input("Geef je bedrag van EUR/USD: "))
bronvaluta = input("Wat is je bronvaluta; EUR of USD: ").strip().upper()
#strip betekent alle ingevoerde tekst als een gewoon basis woord geven, bv. AZIË = azie

if bronvaluta =="EUR":
    doelvaluta = "USD"
    resultaat =bedrag * WISSELKOERS_EUR_NAAR_USD
if bronvaluta == "USD":
    doelvaluta = "EUR"
    resultaat = bedrag / WISSELKOERS_EUR_NAAR_USD

print( f"{bedrag} {bronvaluta} is gelijk aan {resultaat:.2f} {doelvaluta}")
