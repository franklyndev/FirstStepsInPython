cont = ('zero', 'um', 'dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero = int(input("Digite um número entre 0 e 10: "))
    if numero >= 0 and numero <= 10:
        break
    print("Tente novamente!", end = "")
print(f"Voce digitou o número {cont[numero]}")    