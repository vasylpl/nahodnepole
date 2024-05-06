import random

delka_pole = random.randint(1,10)

pole = []

for _ in range(delka_pole):
    pole.append(random.randint(1, 100))

print(pole)