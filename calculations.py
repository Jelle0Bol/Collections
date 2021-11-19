getal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
getal2 = [2, 4 ,6 ,8 ,10, 12 ,14 ,16 ,18, 20]

def plus():
    einde = [getalA + getalB for getalA, getalB in zip(getal1, getal2)]
    print(einde)
def min():
    einde = [getalA - getalB for getalA, getalB in zip(getal1, getal2)]
    print(einde)
def keer():
    einde = [getalA * getalB for getalA, getalB in zip(getal1, getal2)]
    print(einde)
def delen():
    einde = [getalA / getalB for getalA, getalB in zip(getal1, getal2)]
    print(einde)

plus()
min()
keer()
delen()