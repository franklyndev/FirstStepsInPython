lista = []
posicao = 0
for i in range(0, 5):
    num = int(input("Digite um número: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
print(lista)    