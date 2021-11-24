# Nieuw programmatje omdat de andere (MM.py) verkeerd was gemaakt maar wel goed was gemaakt voor de volgende opdracht.

import random

getal = 1

MM = ["Oranje", "Blauw", "Bruin", "Groen"]
aantalMM = int(input("Hoeveel M&M's heeft u? : "))

dictomm={

    "Oranje":0,
    "Blauw":0,
    "Bruin":0,
    "Groen":0,

}

for p in range(1):
    print(random.choice(MM))
    getal + 1
    print(getal)