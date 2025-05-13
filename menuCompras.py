opcao = 0
while opcao != 4:
    
    print("-------------\n   M E N U\n-------------")
    print("[1] Maçã R$2,30")
    print("[2] Banana R$1,80")
    print("[3] Laranja R$2,00")
    print("[4] Sair")
    opcao = int(input("Opção: "))
    if opcao == 4:
        print("Encerrando..")
        break
    quantidade = int(input("Quantidade: "))
    
    def desconto5(total):
        if total > 20 and total < 50:
            desc = total * 5/100 
            totalcomdesc = total - desc
            return totalcomdesc   
    def desconto10(total):
        if total >= 50:
            desc = total * 10/100 
            totalcomdesc = total - desc
            return totalcomdesc     

    if opcao == 1:
        if quantidade > 1: # jf pra plural das frutas
            fruta = "Maçãs"
        else:
            fruta = "Maçã"    
        preco = 2.30        
        total = quantidade * preco
        
    elif opcao == 2:
        if quantidade > 1:
            fruta = "Bananas" # jf pra plural das frutas
        else:
            fruta = "Banana"
        preco = 1.80
        total = quantidade * preco

    elif opcao == 3:
        if quantidade > 1:
            fruta = "Laranjas" # jf pra plural das frutas
        else:
            fruta = "Laranja"
        preco = 2.00 
        total = quantidade * preco
    else:
        print("Opção inválida!")    
    print("---------------\n  COMPROVANTE\n---------------")    
    print(f"Total sem desconto: {total}")        
    if total > 20 and total < 50:
        totalcomdesc = desconto5(total)
        print("Desconto 5%, pagará {:.2f}".format(totalcomdesc))
    elif total > 50:
        totalcomdesc = desconto10(total)
        print("Desconto 10%, pagará {:.2f}".format(totalcomdesc))
    else:     
        print("Você comprou {} {} total sem desconto: {:.2f}".format(quantidade, fruta, total))   