# Programa que conta os pares no intervalo de 1 e 50
print("Contando pares...")
for conta_par in range(1, 51, 1):
    if conta_par % 2 == 0:
        print(f"{conta_par}")
print("Terminei de contar.")        