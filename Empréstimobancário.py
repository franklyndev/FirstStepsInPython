valorcasa = float(input("Valor da casa: ")) # Variável que pergunta o valor da casa
salario = float(input("Seu salário: ")) # Variável que pergunta o salário do comprador
anos = int(input("Quantos anos você pretende pagar: ")) # Variável que pergunta o tempo de parcelamento
percentcasa = salario * 30/100
prestacao = valorcasa / (anos * 12)
if prestacao >= percentcasa:
    print("Empréstimo negado")
    print("Infelizmente você não poderá comprar a casa, pois seu salário foi execedido 30%.")
    print(f"Para pagar uma casa de R${valorcasa} em {anos} anos a prestação será de R${prestacao} por mês e você recebe apenas {salario}")
else:
    print("Empréstimo CONCEDIDO")
    print(f"Para pagar uma casa de R${valorcasa} em {anos} anos a prestação será de R${prestacao} por mês e você ganha R${salario  }")