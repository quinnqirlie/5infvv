def fahrenheit_naar_celsius(temp_f):
    celsius = (temp_f-32)*5/9
    print(f"Het is {celsius} graden Celsius")
    celsius= round(celsius,1)

methode = input("Wil je Fahrenheit of Celsius als uitkomst krijgen?: ").lower()
if methode == "celsius":
    tempF =int(input("Geef een temperatuur in Fahrenheit:"))
else:
    tempC = int(input("Geef een temperatuur in Fahrenheit:"))
    
celsius= round(celsius,1)
print(f"{celsiusR} graden Celsius.")