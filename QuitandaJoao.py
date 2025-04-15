# Quintanda de Seu João
maca = 10
banana = 15
laranja = 20
escolha = 0
while escolha != 4:
  escolha = int(input("--------------------------------------------\n 1 - Realizar uma venda\n 2 - verificar o estoque atual\n 3 - Alterar o estoque(reabasteciemento ou ajuste)\n 4 - Sair do programa\n--------------------------------------------\n Opção: "))
  if escolha == 1:
    print("Realizar Venda\n\nCatálogo:\n 1 - Maçã R$2,50\n 2 - Banana R$1,80\n 3 - Laranja R$2,00\n")
    opcao = int(input("Qual fruta: "))
    
    if opcao == 1:
      
      quantidade = int(input("Quantidade: "))
      if quantidade > maca:
        print("SEM ESTOQUE O SUFICIENTE!")
      else:  
        total =  2.50 * quantidade
        maca = maca - quantidade

        print(f"Você comprou {quantidade} de Maçãs e deu = R${total}")
    
    elif opcao == 2:
    
      quantidade = int(input("Quantidade: "))
      if quantidade > banana:
        print("SEM ESTOQUE O SUFICIENTE!")
      else:  
        total =  1.80 * quantidade
        banana = banana - quantidade
    
        print(f"Você comprou {quantidade} de Bananas e deu = R${total}")

    elif opcao == 3:

        quantidade = int(input("Quantidade: "))
        if quantidade > laranja:
          print("SEM ESTOQUE O SUFICIENTE!")
        else:  
          total =  2.00 * quantidade
          laranja = laranja - quantidade

          print(f"Você comprou {quantidade} de Laranjas e deu = R${total}")
  elif escolha == 2:
    print("Estoque atual: ")
    print("Maçãs: ", maca)
    print("Bananas: ", banana)
    print("Laranjas: ", laranja)

  elif escolha == 3: 
    ajustar = input("Quer adicionar ou remover estoque: ")
    if ajustar == "adicionar":
      decidirfruta = int(input("1 - Maçã\n 2 - Banana\n 3 - Laranja\n"))
      if decidirfruta == 1:
        print (f"Estoque atual de maçã: {maca} ")
        adicao = int(input("Quer adicionar quantas maçãs: "))
        maca = maca + adicao
        print("Estoque atual: ")
        print("Maçãs: ", maca)
        print("Bananas: ", banana)
        print("Laranjas: ", laranja)
      elif decidirfruta == 2:
        print (f"Estoque atual de banana: {banana} ")
        adicao = int(input("Quer adicionar quantas bananas: "))
        banana = banana + adicao
        print("Estoque atual: ")
        print("Maçãs: ", maca)
        print("Bananas: ", banana)
        print("Laranjas: ", laranja)
      elif decidirfruta == 3:
        print (f"Estoque atual de Laranja: {laranja} ")
        adicao = int(input("Quer adicionar quantas laranjas: "))
        laranja = laranja + adicao
        print("Estoque atual: ")
        print("Maçãs: ", maca)
        print("Bananas: ", banana)
        print("Laranjas: ", laranja)
        
    elif ajustar == "remover":
        decidirfruta = int(input("1 - Maçã\n 2 - Banana\n 3 - Laranja"))
        if decidirfruta == 1:
          print (f"Estoque atual de maçã: {maca} ")
          subtracao = int(input("Quer remover quantas maçãs: "))
          maca = maca - subtracao
          print("Estoque atual: ")
          print("Maçãs: ", maca)
          print("Bananas: ", banana)
          print("Laranjas: ", laranja)
        elif decidirfruta == 2:
          print (f"Estoque atual de banana: {banana} ")
          subtracao = int(input("Quer remover quantas bananas: "))
          banana = banana - subtracao
          print("Estoque atual: ")
          print("Maçãs: ", maca)
          print("Bananas: ", banana)
          print("Laranjas: ", laranja)
        elif decidirfruta == 3:
          print (f"Estoque atual de Laranja: {laranja} ")
          subtracao = int(input("Quer remover quantas laranjas: "))
          laranja = laranja - subtracao
          print("Estoque atual: ")
          print("Maçãs: ", maca)
          print("Bananas: ", banana)
          print("Laranjas: ", laranja)
          
  elif  escolha == 4:
    print("Saindo do programa...")