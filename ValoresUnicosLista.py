choice = ""
val = []
i = 0
while choice != "N":
    n = int(input("Digite um número: "))
    if n not in val:
        val.append(n)
    choice = input("Quer continuar?[S/N]: ").upper()
    
print(val)        