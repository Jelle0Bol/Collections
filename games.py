import random
spelList = ["Monopoly", "Yahtzee", "Bridge", "Poker", "Pesten", "Mens erger je niet", "Cluedo"]
nummer = random.randrange(3,10)
for p in range (nummer):
    print (random.choice(spelList))
