# Tabuada do número que o usuário escolher
i = int(input("Digite o número que deseja multiplicar: "))
f = int(input("Digite até quanto quer multiplicar: "))
for f in range(1, f+1):
    result = i * f
    print(f"{i} x {f}= {result}")
print("Terminei de contar")        