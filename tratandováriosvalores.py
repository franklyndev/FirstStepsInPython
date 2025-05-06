numeros = 0
soma = 0
contagem = 0
while numeros < 999:
    numeros = int(input("Digite um número: "))
    if numeros != 999:
        soma += numeros
        contagem += 1
        
print("Soma de todos os números = {}".format(soma))
print(f"foram digitados {contagem} números")           