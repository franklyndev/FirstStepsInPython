import random
import time
usuario = 0
computador = 1
while usuario != computador:
    usuario = int(input("Digite um número: "))
    computador = random.randint(1, 10)
    print("pensando...")
    time.sleep(1)
    print ("pensei em ",computador)
print("Computador: Parabéns você advinhou o número que eu estava pensando!")    
