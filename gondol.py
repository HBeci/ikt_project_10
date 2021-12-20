import random
szam = int(input("adj meg egy számot "))
valtozo = random.randint(1,5)
if szam == valtozo:
    print("ügyes vagy")
if szam > valtozo:
    print("a te számod nagyobb")
else:
    print("a te számod kisebb")