import random
MM = ["Oranje", "Blauw", "Groen", "Bruin"]
AantalMM = int(input("Hoeveel M&M's wilt u toevoegen? : "))

dicmm={

    "Bruin":0,
    "Oranje":0,
    "Blauw":0,
    "Groen":0,
}

groen = 0
blauw = 0
oranje = 0
bruin = 0

def aantalMMM():
    dicmm["Groen"] = groen
    dicmm["Blauw"] = blauw
    dicmm["Oranje"] = oranje
    dicmm["Bruin"] = bruin

def randomMM():
    global zakm, groen, blauw, oranje, bruin, dicmm
    for p in range(AantalMM):
        zakm = random.choice(MM)
        MM.append(zakm)
        groen += zakm.count("Groen")
        blauw += zakm.count("Blauw")
        oranje += zakm.count("Oranje")
        bruin += zakm.count("Bruin")


randomMM()
aantalMMM()
print(dicmm)

