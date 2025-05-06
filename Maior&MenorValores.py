opcao = "s"
maior = 0
menor = 10000
soma = 0
contagem = 0
while opcao == "s":
    numeros = int(input("Digite um número: "))
    if opcao == "s":
        soma += numeros
        contagem += 1   
    if maior < numeros: 
        maior = numeros
    if menor > numeros:
        menor = numeros     
    opcao = input("Quer continuar [S/N]: ").lower()
media = soma / contagem    
print("Média: {:.2f}".format(media))    
print("Maior número: {}".format(maior))
print("Menor número: {}".format(menor))           