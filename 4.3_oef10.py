import random

random = [random.randint(1,100) for _ in range (10)]
print (random)
max = random[9]
min = random[0]
for getal in random:
    if max < getal:
        max = getal

    if min > getal:
        min = getal
print(f"Het maximum is {max}")
print(f"Het minimum is {min}")

