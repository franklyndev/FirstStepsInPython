lanche = ("hambúrger","Suco","Pizza", "Pudim")
#comment Tuplas são imutáveis
#comment lanche[1] = "Pão" = ERRO de atribuição, isso é igual o (val) do Kotlin
#comment Em tuplas posso ter vários tipos de váriável juntos| tupla = ("Franklyn", 18, "abc", 62.56) 
print(lanche)
for c in range(0,len(lanche)):
    print("Eu vou comer", lanche[c])
print("Comi pra caramba!")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

a = (1, 3, 5)
b = (2, 6, 7, 9)
c = a + b
print(a[0])    