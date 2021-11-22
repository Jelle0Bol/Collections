import random

MM = ["Oranje", "Blauw", "Groen", "Bruin"]

AantalMM = int(input("Hoeveel M&M's wilt u toevoegen? : "))

for m in range(AantalMM):
    print (random.choice(MM))

