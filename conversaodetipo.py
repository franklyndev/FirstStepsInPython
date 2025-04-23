numero = int(input("Digite um número: "))
escolha = int(input("Quero transformar esse número em:\n1. Binário\n2. Octal\n3. Hexadecimal\nOpção:  "))
if escolha == 1:
    print("O número {numero} que você digitou em forma binária é=",bin(numero)[2:])
elif escolha == 2:
    print("O número {numero} que você digitou em forma octal é=",oct(numero))
elif escolha == 3: 
    print("O número {numero} que você digitou em forma hexadecimal é=",hex(numero))
else:
    print("O número que você digitou é inválido!")        

