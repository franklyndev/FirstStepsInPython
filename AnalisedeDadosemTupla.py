
tuple = (int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")))
print(tuple)
print(f"Quantas vezes o 9 apareceu: {tuple.count(9)}")
print(f"posição do valor 3: {tuple.index(3)}")
for i in range(4):
    if tuple[i] % 2 == 0:
        print(tuple[i] ,"é par")
        