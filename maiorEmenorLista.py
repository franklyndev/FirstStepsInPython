val = []
maior = 0
menor = 0
for i in range(5):
    val.append(int(input("Digite um número: ")))
    if i == 0:
        maior = menor = val[i]
    else:
        if val[i] > maior:
            maior = val[i]
        if val[i] < menor:
            menor = val[i]        
print("Maior valor:", maior, "posição", )
print("Menor valor:", menor, "posição", )