def bereken_bmi(gewicht, lengte):
    BMI = gewicht/(lengte*lengte)
    BMI=round(BMI,1)
    return BMI

gewicht=int(input("Wat is je gewicht in kg?:"))
lengte=float(input("Wat is je lengte in meters?:"))
print(f"Je BMI is {bereken_bmi(gewicht,lengte)}.")