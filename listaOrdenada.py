numeros = []
for i in range(0, 5):
    n = int(input("Digite um número: "))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
    else: 
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao, n)
                break
            posicao += 1
print(numeros)               