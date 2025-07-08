lista = []
r = ""
while r != "N":
    num = int(input("Digite um número: "))
    lista.append(num)   
    r = input("Vai continuar[S/N]:").upper()
print("A) Números digitados: ",len(lista))
lista.sort(reverse=True)
print(f"B) Lista de valores: ",lista)
if 5 in lista: 
    print("5 foi digitado")
else:
    print("5 não foi digitado")    
