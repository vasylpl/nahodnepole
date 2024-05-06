import random

cislo1 = random.randint(1, 1000)
cislo2 = random.randint(1, 1000)

operator = random.choice(['<', '>', '=='])

podminka = f'{cislo1} {operator} {cislo2}'

if eval(podminka):
    print(f"podminka {podminka} je splněna.")
else:
    print(f"podminka {podminka} neni splněna.")