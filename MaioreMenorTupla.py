from random import randint
# Gambiarra
tuple = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(tuple)
maior = 0
menor = 10000
for i in range(len(tuple)):
    if maior < tuple[i]:
        maior = tuple[i]
    if menor > tuple[i]:
        menor = tuple[i]    
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
