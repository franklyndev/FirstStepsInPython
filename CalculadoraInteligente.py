import random
opcao = 0
soma = 0
multi = 0
maior = 0
while opcao != 5:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        soma = n1 + n2
        print("Resultado: ",soma)
    elif opcao == 2:
        multi = n1 * n2
        print("Resultado: ",multi)
    elif opcao == 3:
        if n1 > n2: 
            maior = n1
        else:
            maior = n2
            print("O número maior é ",maior)
    elif opcao == 4: 
        n1 = random.randint(1,10)
        n2 = random.randint(1,10)
        print("Novo n1 =", n1)
        print("Novo n2 =", n2)
    elif opcao == 5:
        print("Saindo...")
    else:
        print("Erro, digite uma opção válida!")        
    