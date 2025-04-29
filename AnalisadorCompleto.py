velho = 0
somaidade = 0
mulheresmenor = 0
for contador in range(1, 5):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    somaidade += idade
    sexo = input("M/F: ")
    mediaidade = somaidade / 4
    if idade > velho and sexo == "M":
        velho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulheresmenor += 1
print("Média de idade do grupo: {:.0f}".format(mediaidade))
print(f"{nomevelho} é o Homem mais velho com {velho} anos.")    
if mulheresmenor == 1:
    print(f"{mulheresmenor} mulher tem menos de 20 anos")
elif mulheresmenor > 1:
    print(f"{mulheresmenor} mulheres tem menos de 20 anos")
else:
    print(f"Não tem nenhuma mulher com menos de 20 anos")         