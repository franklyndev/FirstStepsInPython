fatorial = 1
numero = int(input("Digite um número: "))
while numero != 0:
    if numero == 1:
        print(f"{numero} = ",end ="")
    else:
        print(f"{numero} x ",end ="")    
    fatorial = fatorial * numero     
    numero = numero - 1
print(fatorial, end = "")    